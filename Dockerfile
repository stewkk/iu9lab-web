FROM golang:bullseye

# Set current timezone
RUN echo "Europe/Moscow" > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y --allow-unauthenticated \
    binutils-dev \
    build-essential \
    curl \
    python3-dev \
    vim \
    sudo \
    wget \
    dirmngr \
    python3-pip


RUN apt-get clean all

RUN --mount=type=cache,src=/var/cache/iu9lab-web/modules,target=/go/pkg/mod \
    --mount=type=cache,src=/var/cache/iu9lab-web/build,target=/root/.cache/go-build \
    go install github.com/deepmap/oapi-codegen/cmd/oapi-codegen@latest
RUN --mount=type=cache,src=/var/cacheiu9lab-web/pip,target=/root/.cache \
    pip3 install yandex-taxi-testsuite[postgresql-binary]

EXPOSE 8080

ENV PATH /usr/sbin:/usr/bin:/sbin:/bin:${PATH}
