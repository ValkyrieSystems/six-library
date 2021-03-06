/* =========================================================================
* This file is part of the CSM SICD Plugin
* =========================================================================
*
* (C) Copyright 2004 - 2014, MDA Information Systems LLC
*
* The CSM SICD Plugin is free software; you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation; either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU Lesser General Public License for more details.
*
* You should have received a copy of the GNU Lesser General Public
* License along with this program; if not,
* see <http://www.gnu.org/licenses/>.
*
*/

#include "Error.h"
#include <sys/OS.h>
#include <sys/Path.h>
#include <six/csm/SICDSensorModel.h>
#include <io/StringStream.h>
#include <logging/NullLogger.h>
#include <six/XMLControlFactory.h>
#include <six/NITFReadControl.h>
#include <six/sicd/ComplexXMLControl.h>
#include <six/sicd/Utilities.h>

namespace six
{
namespace CSM
{
const csm::Version SICDSensorModel::VERSION(1, 1, 1);
const char SICDSensorModel::NAME[] = "SICD_SENSOR_MODEL";

SICDSensorModel::SICDSensorModel(const csm::Isd& isd,
                                 const std::string& dataDir)
{
    setSchemaDir(dataDir);

    const std::string& format(isd.format());

    if (format == "NITF2.1")
    {
        // NOTE: Used dynamic_cast here previously but using it with IAI's
        //       version of vts, it threw an exception.  Did older versions of
        //       vts not use the /GR flag (they've since reported it worked
        //       fine when our plugin used dynamic_cast)?
        initializeFromISD((const csm::Nitf21Isd&)isd);
    }
    else if (format == "FILENAME")
    {
        // Note: this case has not been tested
        initializeFromFile(isd.filename());
    }
    else
    {
        throw csm::Error(csm::Error::SENSOR_MODEL_NOT_CONSTRUCTIBLE,
                           "Unsupported ISD format " + format,
                           "SICDSensorModel::constructModelFromISD");
    }
}

SICDSensorModel::SICDSensorModel(const std::string& sensorModelState,
                                 const std::string& dataDir)
{
    setSchemaDir(dataDir);
    replaceModelStateImpl(sensorModelState);
}

void SICDSensorModel::initializeFromFile(const std::string& pathname)
{
    try
    {
        // create an XML registry
        // The reason to do this is to avoid adding XMLControlCreators to the
        // XMLControlFactory singleton - this way has more fine-grained control
        six::XMLControlRegistry xmlRegistry;
        xmlRegistry.addCreator(six::DataType::COMPLEX,
                new six::XMLControlCreatorT<six::sicd::ComplexXMLControl>());

        // create a reader and load the file
        six::NITFReadControl reader;
        reader.setXMLControlRegistry(&xmlRegistry);
        reader.load(pathname, mSchemaDirs);

        six::Container* const container = reader.getContainer();
        if (container->getDataType() != six::DataType::COMPLEX ||
            container->getNumData() != 1 ||
            container->getData(0)->getDataType() != six::DataType::COMPLEX)
        {
            throw csm::Error(csm::Error::SENSOR_MODEL_NOT_CONSTRUCTIBLE,
                               "Not a SICD",
                               "SICDSensorModel::initializeFromFile");
        }

        mData.reset(reinterpret_cast<six::sicd::ComplexData*>(
                container->getData(0)));
        container->removeData(mData.get());

        // get xml as string for sensor model state
        std::string xmlStr = six::toXMLString(mData.get(), &xmlRegistry);
        mSensorModelState = NAME + std::string(" ") + xmlStr;
        reinitialize();
    }
    catch (const except::Exception& ex)
    {
        throw csm::Error(csm::Error::SENSOR_MODEL_NOT_CONSTRUCTIBLE,
                           ex.getMessage(),
                           "SICDSensorModel::initializeFromFile");
    }
}

void SICDSensorModel::initializeFromISD(const csm::Nitf21Isd& isd)
{
    try
    {
        // Check for the first SICD DES and parse it
        xml::lite::Document* sicdXML = NULL;
        xml::lite::MinidomParser domParser;

        const std::vector< csm::Des>& desList(isd.fileDess());
        for (size_t ii = 0; ii < desList.size(); ++ii)
        {
            const std::string& desData(desList[ii].data());

            if (!desData.empty())
            {
                try
                {
                    io::StringStream stream;
                    stream.write(desData.c_str(), desData.length());

                    domParser.clear();
                    domParser.parse(stream);

                    const std::string localName = domParser.getDocument()->
                            getRootElement()->getLocalName();
                    if (localName == "SICD")
                    {
                        sicdXML = domParser.getDocument();
                        break;
                    }
                    else if (localName == "SIDD")
                    {
                        // SIDD NITFs may also contain SICD DESs (that describe
                        // the SICD that this SIDD was derived from).  I guess
                        // technically we could build up a sensor model from
                        // this, but it seems more correct to error out so that
                        // the SIDDSensorModel will get used.  Note that a SIDD
                        // DES will always appear prior to a SICD DES, so if we
                        // do encounter a SICD DES before this point, we can
                        // safely say it's a SICD NITF.
                        throw csm::Error(csm::Error::UNKNOWN_ERROR,
                                           "SIDD, not SICD, NITF",
                                           "SICDSensorModel::SICDSensorModel");
                    }
                }
                catch(const except::Exception& )
                {
                    // Couldn't parse DES as xml -- it's not a sicd so skip it
                }
            }
        }

        if (sicdXML == NULL)
        {
            throw csm::Error(csm::Error::UNKNOWN_ERROR,
                               "Not a SICD",
                               "SICDSensorModel::SICDSensorModel");
        }

        // get xml as string for sensor model state
        io::StringStream stringStream;
        sicdXML->getRootElement()->print(stringStream);
        mSensorModelState = NAME + std::string(" ") + stringStream.stream().str();

        six::XMLControlRegistry xmlRegistry;
        xmlRegistry.addCreator(six::DataType::COMPLEX,
                new six::XMLControlCreatorT<six::sicd::ComplexXMLControl>());

        logging::NullLogger logger;
        std::auto_ptr<six::XMLControl> control(
                xmlRegistry.newXMLControl(six::DataType::COMPLEX, &logger));

        mData.reset(reinterpret_cast<six::sicd::ComplexData*>(control->fromXML(
                sicdXML, mSchemaDirs)));
        reinitialize();
    }
    catch (const except::Exception& ex)
    {
        throw csm::Error(csm::Error::SENSOR_MODEL_NOT_CONSTRUCTIBLE,
                           ex.getMessage(),
                           "SICDSensorModel::initializeFromISD");
    }
}

bool SICDSensorModel::containsComplexDES(const csm::Nitf21Isd& isd)
{
    xml::lite::MinidomParser domParser;

    const std::vector< csm::Des>& desList(isd.fileDess());
    for (size_t ii = 0; ii < desList.size(); ++ii)
    {
        const std::string& desData(desList[ii].data());

        if (!desData.empty())
        {
            try
            {
                io::StringStream stream;
                stream.write(desData.c_str(), desData.length());

                domParser.clear();
                domParser.parse(stream);

                const std::string localName = domParser.getDocument()->
                        getRootElement()->getLocalName();
                if (localName == "SICD")
                {
                    return true;
                }
                else if (localName == "SIDD")
                {
                    // SIDD NITFs may also contain SICD DESs (that describe the
                    // SICD that this SIDD was derived from).  I guess
                    // technically we could build up a sensor model from this,
                    // but it seems more correct to return false so that the
                    // SIDDSensorModel gets picked.  Note that a SIDD DES will
                    // always appear prior to a SICD DES, so if we do encounter
                    // a SICD DES before this point, we can safely say it's a
                    // SICD NITF.
                    return false;
                }
            }
            catch(const except::Exception& )
            {
                // Couldn't parse DES as xml -- it's not a sicd so skip it
            }
        }
    }

    return false;
}

csm::Version SICDSensorModel::getVersion() const
{
    return VERSION;
}

std::string SICDSensorModel::getModelName() const
{
    return NAME;
}

std::string SICDSensorModel::getPedigree() const
{
    return (mData->getSource() + "_" + NAME + "_SAR");
}

std::string SICDSensorModel::getImageIdentifier() const
{
    return mData->getName();
}

void SICDSensorModel::setImageIdentifier(const std::string& imageId,
                                         csm::WarningList* )

{
    mData->setName(imageId);
}

std::string SICDSensorModel::getSensorIdentifier() const
{
    return mData->getSource();
}

std::string SICDSensorModel::getPlatformIdentifier() const
{
    return mData->getSource();
}

std::string SICDSensorModel::getCollectionIdentifier() const
{
    // same as imageIdentifier right now...
    return mData->collectionInformation->coreName;
}

std::string SICDSensorModel::getSensorMode() const
{
    switch (mData->collectionInformation->radarMode)
    {
    case six::RadarModeType::SPOTLIGHT:
        return CSM_SENSOR_MODE_SPOT;
    case six::RadarModeType::STRIPMAP:
    case six::RadarModeType::DYNAMIC_STRIPMAP:
        return CSM_SENSOR_MODE_STRIP;
    default:
        return CSM_SENSOR_MODE_FRAME;
    }
}

six::DateTime SICDSensorModel::getReferenceDateAndTimeImpl() const
{
    return mData->timeline->collectStart;
}

types::RowCol<double>
SICDSensorModel::toPixel(const types::RowCol<double>& pos) const
{
    const six::sicd::ImageData& imageData(*mData->imageData);
    const types::RowCol<double> aoiOffset(imageData.firstRow,
                                          imageData.firstCol);

    const types::RowCol<double> offset(
            imageData.scpPixel.row - aoiOffset.row,
            imageData.scpPixel.col - aoiOffset.col);

    return types::RowCol<double>(
            (pos.row / mData->grid->row->sampleSpacing) + offset.row,
            (pos.col / mData->grid->col->sampleSpacing) + offset.col);
}

types::RowCol<double>
SICDSensorModel::fromPixel(const csm::ImageCoord& pos) const
{
    const six::sicd::ImageData& imageData(*mData->imageData);
    const types::RowCol<double> aoiOffset(imageData.firstRow,
                                          imageData.firstCol);

    const types::RowCol<double> adjustedPos(
            pos.line - (imageData.scpPixel.row - aoiOffset.row),
            pos.samp - (imageData.scpPixel.col - aoiOffset.col));

    return types::RowCol<double>(
            adjustedPos.row * mData->grid->row->sampleSpacing,
            adjustedPos.col * mData->grid->col->sampleSpacing);
}

types::RowCol<double>
SICDSensorModel::getSampleSpacing() const
{
    return types::RowCol<double>(mData->grid->row->sampleSpacing,
                                 mData->grid->col->sampleSpacing);
}

csm::ImageVector SICDSensorModel::getImageSize() const
{
    return csm::ImageVector(mData->getNumRows(), mData->getNumCols());
}

void SICDSensorModel::replaceModelStateImpl(const std::string& sensorModelState)
{
    const size_t idx = sensorModelState.find(' ');
    if (idx == std::string::npos)
    {
        throw csm::Error(csm::Error::INVALID_SENSOR_MODEL_STATE,
                           "Invalid sensor model state",
                           "SICDSensorModel::replaceModelStateImpl");
    }

    const std::string sensorModelName = sensorModelState.substr(0, idx);
    if (sensorModelName != NAME)
    {
        throw csm::Error(csm::Error::INVALID_SENSOR_MODEL_STATE,
                           "Invalid sensor model state",
                           "SICDSensorModel::replaceModelStateImpl");
    }

    const std::string sensorModelXML = sensorModelState.substr(idx + 1);

    try
    {
        io::StringStream stream;
        stream.write(sensorModelXML.c_str(), sensorModelXML.length());

        xml::lite::MinidomParser domParser;
        domParser.parse(stream);

        six::XMLControlRegistry xmlRegistry;
        xmlRegistry.addCreator(six::DataType::COMPLEX,
                new six::XMLControlCreatorT<six::sicd::ComplexXMLControl>());

        logging::NullLogger logger;
        std::auto_ptr<six::XMLControl> control(
                xmlRegistry.newXMLControl(six::DataType::COMPLEX, &logger));

        // get xml as string for sensor model state
        mSensorModelState = sensorModelState;

        mData.reset(reinterpret_cast<six::sicd::ComplexData*>(control->fromXML(
                domParser.getDocument(), mSchemaDirs)));
        reinitialize();
    }
    catch (const except::Exception& ex)
    {
        throw csm::Error(csm::Error::INVALID_SENSOR_MODEL_STATE,
                           ex.getMessage(),
                           "SICDSensorModel::replaceModelStateImpl");
    }
}

void SICDSensorModel::reinitialize()
{
    mGeometry.reset(six::sicd::Utilities::getSceneGeometry(mData.get()));

    mProjection.reset(six::sicd::Utilities::getProjectionModel(
            mData.get(),
            mGeometry.get()));

    std::fill_n(mAdjustableTypes,
                static_cast<size_t>(scene::AdjustableParams::NUM_PARAMS),
                csm::param::REAL);

    // NOTE: See member variable definition in header for why we're doing this
    mSensorCovariance = mProjection->getErrorCovariance(
            mGeometry->getReferencePosition());
}
}
}
