#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname $DIR)"
DOCKER_COMPOSE_OPTIONS="-f $DIR/docker-compose.yaml"
DOCKER_OPTIONS="-f $DIR/Dockerfile"

export DOCKER_BUILDKIT=1

# docker build $DOCKER_OPTIONS -t app_dependencies $PARENT_DIR

# docker run --rm -v app_dependencies:/usr/local/lib/python3.8/site-packages app_dependencies

# docker run --name app_dependencies_container -v app_dependencies-volume:/dependencies app_dependencies

docker-compose $DOCKER_COMPOSE_OPTIONS up --remove-orphans --build -d "$@"