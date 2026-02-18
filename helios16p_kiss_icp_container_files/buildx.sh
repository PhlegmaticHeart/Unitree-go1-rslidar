#!/bin/bash

#Build an image based on the secrets file passwd.txt, if you want to change users password, please, edit passwd.txt

set -e

IMAGE_NAME="helios16p-kiss"
TAG="latest_arm64"
PLATFORM="arm64"  # Auto-detect

echo "Build for platform: $PLATFORM"

docker buildx build \
  --platform "linux/$PLATFORM" \
  --tag "$IMAGE_NAME:$TAG" \
  --secret id=pusrs,src=$PWD/passwd.txt \
  --load .

echo "Build completed for $PLATFORM, now it is possible to execute run.sh"

