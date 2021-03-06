/*
 * =========================================================================
 * This file is part of six.sicd-python 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2015, MDA Information Systems LLC
 *
 * six.sicd-python is free software; you can redistribute it and/or modify
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
 */

%module(package="pysix") six_sicd

%feature("autodoc", "1");

%{

#include <complex>
#include <utility>

#include "import/mem.h"
#include "import/six.h"
#include "import/six/sicd.h"

using namespace six::sicd;
using namespace six;

six::sicd::ComplexData * asComplexData(six::Data* data);

/* Need this because we can't really do it on the python side of things */
six::sicd::ComplexData * asComplexData(six::Data* data) 
{
  six::sicd::ComplexData * complexData = dynamic_cast<six::sicd::ComplexData*>(data);
  if( !complexData )
  {
    throw except::BadCastException();
  }
  else 
  {
    return complexData;
  }
}


%}

%include "std_vector.i"
%include "std_string.i"
%include "std_complex.i"
%include "std_pair.i"

%import "math_poly.i"
%import "six.i"
%import "io.i"
%import "mem.i"

/* wrap around auto_ptr */
%inline 
%{
six::sicd::ComplexData * getComplexData( const std::string& sicdPathname, const std::vector<std::string>& schemaPaths ) {
  std::auto_ptr<six::sicd::ComplexData> retv = Utilities::getComplexData(sicdPathname, schemaPaths);
  return retv.release();
}
%}

/* wrap that function defined in the header section */
six::sicd::ComplexData * asComplexData(six::Data* data);

/* this version of the function returns the auto_ptr, ignore it */
%rename ("$ignore", fullname=1) "six::sicd::Utilities::getComplexData";

/* prevent name conflicts */
%rename ("SixSicdUtilities") six::sicd::Utilities;

%include "six/sicd/ComplexClassification.h"
%include "six/sicd/CollectionInformation.h"
%include "six/sicd/ImageCreation.h"
%include "six/sicd/ImageData.h"
%include "six/sicd/GeoData.h"
%include "six/sicd/Grid.h"
%include "six/sicd/Timeline.h"
%include "six/sicd/Position.h"
%include "six/sicd/RadarCollection.h"
%include "six/sicd/ImageFormation.h"
%include "six/sicd/SCPCOA.h"
%include "six/sicd/Antenna.h"
%include "six/sicd/MatchInformation.h"
%include "six/sicd/PFA.h"
%include "six/sicd/RMA.h"
%include "six/sicd/RgAzComp.h"
%include "six/sicd/ComplexData.h"
%include "six/sicd/ComplexXMLControl.h"
%include "six/sicd/Utilities.h"

/* We need this because SWIG cannot do it itself, for some reason */
/* TODO: write script to generate all of these instantiations for us? */

SCOPED_CLONEABLE(six::sicd, CollectionInformation)
SCOPED_CLONEABLE(six::sicd, ImageCreation)
SCOPED_CLONEABLE(six::sicd, ImageData)
SCOPED_CLONEABLE(six::sicd, GeoData)
SCOPED_CLONEABLE(six::sicd, Grid)
SCOPED_COPYABLE(six::sicd, Timeline)
SCOPED_COPYABLE(six::sicd, Position)
SCOPED_COPYABLE(six::sicd, RcvAPC)
SCOPED_CLONEABLE(six::sicd, RadarCollection)
SCOPED_COPYABLE(six::sicd, ImageFormation)
SCOPED_COPYABLE(six::sicd, SCPCOA)
SCOPED_COPYABLE(six::sicd, Antenna)
SCOPED_COPYABLE(six::sicd, MatchInformation)
SCOPED_COPYABLE(six::sicd, SlowTimeDeskew)
SCOPED_COPYABLE(six::sicd, PFA)
SCOPED_COPYABLE(six::sicd, RMA)
SCOPED_COPYABLE(six::sicd, RgAzComp)

SCOPED_CLONEABLE(six::sicd, GeoInfo) 
%template(VectorScopedCloneableGeoInfo) std::vector<mem::ScopedCloneablePtr<six::sicd::GeoInfo> >;
%template(VectorLatLon) std::vector<scene::LatLon>;

SCOPED_COPYABLE(six::sicd, AntennaParameters)
SCOPED_COPYABLE(six::sicd, ElectricalBoresight)
SCOPED_COPYABLE(six::sicd, HalfPowerBeamwidths)
SCOPED_COPYABLE(six::sicd, GainAndPhasePolys)

SCOPED_COPYABLE(six::sicd, MatchType)
SCOPED_COPYABLE(six::sicd, WeightType)

%template(VectorPolyXYZ) std::vector<math::poly::OneD<Vector3> >;

SCOPED_CLONEABLE(six::sicd, DirectionParameters)

SCOPED_CLONEABLE(six::sicd, AreaPlane)
SCOPED_CLONEABLE(six::sicd, AreaDirectionParameters)
SCOPED_CLONEABLE(six::sicd, Segment)
SCOPED_CLONEABLE(six::sicd, TxStep)
SCOPED_CLONEABLE(six::sicd, WaveformParameters)
SCOPED_CLONEABLE(six::sicd, Area)
SCOPED_CLONEABLE(six::sicd, ChannelParameters)
%template(VectorScopedCloneableWaveformParameters) std::vector<mem::ScopedCloneablePtr<six::sicd::WaveformParameters> >;
%template(VectorScopedCloneableTxStep)             std::vector<mem::ScopedCloneablePtr<six::sicd::TxStep> >;
%template(vectorScopedClonableSegment)             std::vector<mem::ScopedCloneablePtr<six::sicd::Segment> >;
%template(VectorScopedCloneableChannelParameters)  std::vector<mem::ScopedCloneablePtr<six::sicd::ChannelParameters> >;
%template(VectorInt)                               std::vector<int>;
SCOPED_COPYABLE(six::sicd, RcvChannelProcessed)
%template(VectorProcessing)                        std::vector<six::sicd::Processing>;
SCOPED_COPYABLE(six::sicd, PolarizationCalibration)
SCOPED_COPYABLE(six::sicd, Distortion)

%template(VectorMatchCollect)                      std::vector<six::sicd::MatchCollect>;
%template(VectorScopedCopyableMatchType)           std::vector<mem::ScopedCopyablePtr<six::sicd::MatchType> >;

SCOPED_COPYABLE(six::sicd, RMAT)
SCOPED_COPYABLE(six::sicd, RMCR)
SCOPED_COPYABLE(six::sicd, INCA)

SCOPED_COPYABLE(six::sicd, InterPulsePeriod)
%template(VectorTimelineSet)                       std::vector<six::sicd::TimelineSet>;

%{
    void getWidebandData(const std::string& sicdPathname, const std::vector<std::string>& schemaPaths, six::sicd::ComplexData* complexData, long arrayBuffer)
    {
        std::complex<float>* realBuffer = reinterpret_cast< std::complex<float>* >(arrayBuffer);
        Utilities::getWidebandData(sicdPathname, schemaPaths, *complexData, realBuffer);
    }
%}

void getWidebandData(std::string sicdPathname, const std::vector<std::string>& schemaPaths, six::sicd::ComplexData* complexData, long arrayBuffer);

%pythoncode %{
import numpy as np
from six_base import VectorString

def read(inputPathname, schemaPaths = VectorString()):
    complexData = getComplexData(inputPathname, schemaPaths)
    
    #Numpy has no concept of complex integers, so dtype will always be complex64
    widebandData = np.empty(shape = (complexData.getNumRows(), complexData.getNumCols()), dtype = "complex64")
    widebandBuffer, ro = widebandData.__array_interface__["data"]
    
    getWidebandData(inputPathname, schemaPaths, complexData, widebandBuffer)
    
    return widebandData, complexData
%}
