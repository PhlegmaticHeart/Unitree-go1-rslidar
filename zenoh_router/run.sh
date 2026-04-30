#!/bin/bash

SCRIPTFOLDER=$( dirname $0 )

docker run --name zenoh_router_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=3 \
  -e ROS_DISTRO=humble \
  -v $SCRIPTFOLDER/entrypoint.sh:/entrypoint.sh \
  -v $SCRIPTFOLDER/cyclonedds_config.xml:/cyclonedds_config.xml \
  -v $SCRIPTFOLDER/entrypoint.sh:/entrypoint.sh \
  -v $SCRIPTFOLDER/zenoh_config_zeppelin.json:/zenoh_config_zeppelin.json \
  --entrypoint "/entrypoint.sh" \
  eclipse/zenoh-bridge-ros2dds:1.8.0
