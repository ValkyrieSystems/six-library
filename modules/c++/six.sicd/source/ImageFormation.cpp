/* =========================================================================
 * This file is part of six.sicd-c++
 * =========================================================================
 *
 * (C) Copyright 2004 - 2014, MDA Information Systems LLC
 *
 * six.sicd-c++ is free software; you can redistribute it and/or modify
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
#include "six/sicd/ImageFormation.h"

using namespace six;
using namespace six::sicd;

ImageFormation::ImageFormation() :
    segmentIdentifier(Init::undefined<std::string>()),
    rcvChannelProcessed(new RcvChannelProcessed()),
    txRcvPolarizationProc(DualPolarizationType::NOT_SET),
    imageFormationAlgorithm(ImageFormationType::PFA),
    tStartProc(Init::undefined<double>()),
    tEndProc(Init::undefined<double>()),
    txFrequencyProcMin(Init::undefined<double>()),
    txFrequencyProcMax(Init::undefined<double>()),
    slowTimeBeamCompensation(SlowTimeBeamCompensationType::NO),
    imageBeamCompensation(ImageBeamCompensationType::NO),
    azimuthAutofocus(AutofocusType::NO),
    rangeAutofocus(AutofocusType::NO)
{
}

