/**
* Lab generator API.
* Can be used to generate laboratory works reports for BMSTU IU9. 
*
* OpenAPI spec version: 0.0.1
* 
*
* NOTE: This class is auto generated by the swagger code generator program.
* https://github.com/swagger-api/swagger-codegen.git
* Do not edit the class manually.
*/
#include "ModelBase.h"

namespace io {
namespace swagger {
namespace server {
namespace model {

ModelBase::ModelBase()
{
}
ModelBase::~ModelBase()
{
}

std::string ModelBase::toJson( const std::string& value )
{
    return value;
}

std::string ModelBase::toJson( const std::time_t& value )
{
    char buf[sizeof "2011-10-08T07:07:09Z"];
    strftime(buf, sizeof buf, "%FT%TZ", gmtime(&value));
    return buf;
}

int32_t ModelBase::toJson( int32_t value )
{
    return value;
}

int64_t ModelBase::toJson( int64_t value )
{
    return value;
}

double ModelBase::toJson( double value )
{
    return value;
}

bool ModelBase::toJson( bool value )
{
    return value;
}

nlohmann::json ModelBase::toJson( std::shared_ptr<ModelBase> content )
{
    return content.get() ? content->toJson() : nlohmann::json();
}

}
}
}
}
