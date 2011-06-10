/* =========================================================================
 * This file is part of six-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * six-c++ is free software; you can redistribute it and/or modify
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
 * License along with this program; If not, 
 * see <http://www.gnu.org/licenses/>.
 *
 */
#include <memory>

#include "six/XMLControlFactory.h"

using namespace six;

XMLControl* XMLControlRegistry::newXMLControl(DataType dataType) const
{
    std::map<DataType, XMLControlCreator*>::const_iterator it;
    it = mRegistry.find(dataType);
    if (it == mRegistry.end())
    {
        throw except::NoSuchKeyException(Ctxt(FmtX("No data class creator %d",
                                                           (int) dataType)));
    }
    return it->second->newXMLControl();
}

//!  Destructor
XMLControlRegistry::~XMLControlRegistry()
{
    for (std::map<DataType, XMLControlCreator*>::iterator p = mRegistry.begin(); p
            != mRegistry.end(); ++p)
    {
        if (p->second)
            delete p->second;
    }
    mRegistry.clear();

}

XMLControl* XMLControlRegistry::newXMLControl(std::string identifier) const
{
    DataType dataType;

    if (identifier == "SICD_XML")
    {
        dataType = DataType::COMPLEX;
    }
    else if (identifier == "SIDD_XML")
    {
        dataType = DataType::DERIVED;
    }

    return newXMLControl(dataType);
}

char* six::toXMLCharArray(const Data* data,
                          const six::XMLControlRegistry *xmlRegistry)
{
    const std::string xml = toXMLString(data, xmlRegistry);
    char* const raw = new char[xml.length() + 1];
    strcpy(raw, xml.c_str());
    return raw;
}

std::string six::toXMLString(const Data* data,
                             const six::XMLControlRegistry *xmlRegistry)
{
    if (!xmlRegistry)
    {
        xmlRegistry = &XMLControlFactory::getInstance();
    }

    const std::auto_ptr<XMLControl>
        xmlControl(xmlRegistry->newXMLControl(data->getDataType()));
    const std::auto_ptr<xml::lite::Document> doc(xmlControl->toXML(data));

    io::ByteStream bs;
    doc->getRootElement()->print(bs);

    return bs.stream().str();
}
