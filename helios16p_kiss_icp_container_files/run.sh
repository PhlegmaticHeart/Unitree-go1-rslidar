#!/bin/bash

#Run the helios-mola container

set -e

IMAGE_NAME="helios16p-kiss"
TAG="latest"
PLATFORM=$(docker info --format '{{.Architecture}}')  # Auto-detect

echo "Starting $IMAGE_NAME"

docker run \
  --rm \
  -it \
  --privileged \
  --network=host \
  "$IMAGE_NAME:$TAG"

# Actually the container dialogue directly with your host connection.
# The container actually can uses display sharing with the host, to do this exec into you shell [  xhost +local:docker  ] command and add the following parameter to the docker run command into this script [ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY ] for debugging purposes. comment the related linea for disabling this.
# After the end of the session, the container will be removed to not waste storage while not in use
