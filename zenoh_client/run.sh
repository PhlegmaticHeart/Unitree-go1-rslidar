#!/bin/bash

docker run --name zenoh_client_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=7 \
  -e ROS_DISTRO=humble \
  -e ROS_LOCALHOST_ONLY=1 \
  --entrypoint "/entrypoint.sh" \
  zenoh:custom_client
