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
#ifndef __SIX_SICD_UTILITIES_H__
#define __SIX_SICD_UTILITIES_H__

#include <memory>
#include <string>
#include <vector>

#include <scene/SceneGeometry.h>
#include <scene/ProjectionModel.h>
#include <six/sicd/ComplexData.h>

namespace six
{
namespace sicd
{
class Utilities
{
public:
    static scene::SceneGeometry* getSceneGeometry(const ComplexData* data);

    static scene::ProjectionModel* getProjectionModel(const ComplexData* data, 
            const scene::SceneGeometry* geom);

    /*
     * Given a SICD pathname and list of schemas, provides a representation
     * of the SICD XML as a ComplexData object
     *
     * \param sicdPathname SICD NITF pathname
     * \param schemaPaths One or more files or directories containing SICD
     * schemas
     *
     * \return ComplexData associated with the SICD NITF
     *
     * \throws except::Exception if file is not a SICD
     */
    static
    std::auto_ptr<ComplexData> getComplexData(
            const std::string& sicdPathname,
            const std::vector<std::string>& schemaPaths);

    /*
     * Given a SICD pathname and list of schemas, provides a representation
     * of the SICD pixel data in a buffer
     *
     * \param sicdPathname SICD NITF pathname
     * \param schemaPaths One or more files or directories containing SICD
     * schemas
     * \param complexData The ComplexData object associated with the SICD
     * \param buffer The pre-sized buffer to be read into
     *
     * \throws except::Exception if the pixel type of the SICD is not a complex
     * float32 or complex int16
     */
    static
    void getWidebandData(
            const std::string& sicdPathname,
            const std::vector<std::string>& schemaPaths,
            const ComplexData& complexData,
            std::complex<float>* buffer);
};
}
}
#endif

