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
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=$DISPLAY \
  "$IMAGE_NAME:$TAG" 
