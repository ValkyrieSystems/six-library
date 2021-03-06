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
#ifndef __SIX_SCPCOA_H__
#define __SIX_SCPCOA_H__

#include "six/Init.h"
#include "six/Types.h"
#include "six/Parameter.h"

namespace six
{
namespace sicd
{
/*!
 *  \struct SCPCOA
 *  \brief SICD SCPCOA parameter
 *
 *  Required parameters describing the COA for the scene center point
 */
struct SCPCOA
{
    
    /*!
     *  Constructor.  All fields are set as undefined, and all fields
     *  are required, and so, must be filled in.
     */
    SCPCOA();

    //! Center of aperture time for the SCP at t_COA_SCP(collectionStart)
    double scpTime;

    //! ARP position at t_COA_SCP in ECEF
    Vector3 arpPos;

    //! ARP velocity at t_COA_SCP in ECEF
    Vector3 arpVel;

    //! ARP acceleration at t_COA_SCP in ECEF
    Vector3 arpAcc;

    //!  Look direction
    SideOfTrackType sideOfTrack;

    //!  Magnitude of the range vector
    double slantRange;

    //! Magnitude of the range vector projected into the ground, with ARP
    //! at nadir
    double groundRange;

    //! The doppler cone angle to SCP at t_COA_SCP
    double dopplerConeAngle;

    //! Grazing angle between the line of sight and ETP
    double grazeAngle;

    //! Incidence angle between SCP LOS and ETP normal
    double incidenceAngle;

    //!  angle between cross range in ETP and cross range in slant plane
    double twistAngle;

    //!  Slope angle from ETP to slant plane at t_COA_SCP
    double slopeAngle;

    //! Angle from north to the line from the SCP to
    //  the ARP Nadir at COA. Measured clockwise
    //  in the ETP.
    //  Added in 1.0.0
    double azimAngle;

    //! Angle from north to the layover direction in
    //  the ETP at COA. Measured clockwise in the
    //  ETP.
    //  Added in 1.0.0
    double layoverAngle;
};

}
}
#endif

