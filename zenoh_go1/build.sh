#!/bin/bash

#Build an image based on the secrets file passwd.txt, if you want to change users password, please, edit passwd.txt

set -e

IMAGE_NAME="zenoh"
TAG="custom_router"
PLATFORM=$(docker info --format '{{.Architecture}}')  # Auto-detect

echo "Build for platform: $PLATFORM"

docker build \
  --tag "$IMAGE_NAME:$TAG" \
  .

echo "Build completed for $PLATFORM, now it is possible to execute run.sh"

