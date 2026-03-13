#!/bin/bash

docker run --name zenoh_router_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=3 \
  -e ROS_DISTRO=humble \
  --entrypoint "/entrypoint.sh" \
  zenoh:custom_router
