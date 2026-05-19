#!/bin/bash

SCRIPTFOLDER=$( dirname $0 )

docker run --name zenoh_client_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=7 \
  -e ROS_DISTRO=humble \
  -e ROS_LOCALHOST_ONLY=1 \
  -e CYCLONEDDS_URI=/cyclonedds_config.xml \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
  -v $SCRIPTFOLDER/entrypoint.sh:/entrypoint.sh \
  -v $SCRIPTFOLDER/cyclonedds_config.xml:/cyclonedds_config.xml \
  -v $SCRIPTFOLDER/zenoh_config_client_iot.json:/zenoh_config_client_iot.json \
  -v $SCRIPTFOLDER/zenoh_config_peer.json:/zenoh_config_peer.json \
  --entrypoint "/entrypoint.sh" \
  eclipse/zenoh-bridge-ros2dds:1.8.0
