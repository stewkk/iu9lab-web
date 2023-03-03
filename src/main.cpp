#include "pistache/endpoint.h"
#include "pistache/http.h"
#include "pistache/router.h"

#include "swagger/impl/DefaultApiImpl.h"

using namespace io::swagger::server::api;

int main() {
    Pistache::Address addr(Pistache::Ipv4::any(), Pistache::Port(8080));

    DefaultApiImpl server(addr);
    server.init(2);
    server.start();

    server.shutdown();
}

