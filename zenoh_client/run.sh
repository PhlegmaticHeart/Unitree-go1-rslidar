#!/bin/bash

docker run --name zenoh_client_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=7 \
  -e ROS_DISTRO=humble \
  -e ROS_LOCALHOST_ONLY=1 \
  --mount type=bind,source=$PWD/entrypoint.sh,target=/entrypoint.sh \
  --mount type=bind,source=$PWD/cyclonedds_config.xml,target=/cyclonedds_config.xml \
  --mount type=bind,source=$PWD/zenoh_config_zeppelin.json,target=/zenoh_config_zeppelin.json \
  --mount type=bind,source=$PWD/zenoh_config_links_guest.json,target=/zenoh_config_links_guest.json \
  --entrypoint "/entrypoint.sh" \
  eclipse/zenoh-bridge-ros2dds:1.8.0
