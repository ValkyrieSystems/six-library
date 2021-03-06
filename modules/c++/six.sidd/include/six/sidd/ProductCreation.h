/* =========================================================================
 * This file is part of six.sidd-c++
 * =========================================================================
 *
 * (C) Copyright 2004 - 2014, MDA Information Systems LLC
 *
 * six.sidd-c++ is free software; you can redistribute it and/or modify
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
#ifndef __SIX_PRODUCT_CREATION_H__
#define __SIX_PRODUCT_CREATION_H__

#include <memory>

#include "six/Types.h"
#include "six/Init.h"
#include "six/ParameterCollection.h"
#include "six/sidd/DerivedClassification.h"

namespace six
{
namespace sidd
{
struct ProcessorInformation
{
    std::string application;
    DateTime processingDateTime;
    std::string site;

    // Optional
    std::string profile;
    ProcessorInformation* clone() const;
};

/*!
 *  \struct ProductCreation
 *  \brief SIDD ProductCreation parameters
 *
 *  Contains general information about product creation
 */
class ProductCreation
{
public:
    //!  Allocate mandatory processorInformation
    ProductCreation() :
        processorInformation(new ProcessorInformation())
    {
    }

    //!  Clone this, including processorInformation
    ProductCreation* clone() const;

    //!  Details regarding processor
    mem::ScopedCloneablePtr<ProcessorInformation> processorInformation;

    //!  The overall classification of the product
    DerivedClassification classification;

    //!  The output product name defined by the processor
    std::string productName;

    //!  Class of product.
    std::string productClass;

    /*! 
     *  (Optional) type of sub-product. 
     *  Leave this blank if none
     */
    std::string productType;

    /*!
     *  (Optional, Unbounded) Extensible params used to support
     *  profile-specific needs related to product creation
     */
    ParameterCollection productCreationExtensions;
};
}
}
#endif

