#!/bin/bash

SCRIPTFOLDER=$( dirname $0 )

docker run --name zenoh_client_container \
  --rm -it --network=host \
  -e ROS_DOMAIN_ID=7 \
  -e ROS_DISTRO=humble \
  -e ROS_LOCALHOST_ONLY=0 \
  -v $SCRIPTFOLDER/entrypoint.sh:/entrypoint.sh \
  -v $SCRIPTFOLDER/cyclonedds_config.xml:/cyclonedds_config.xml \
  -v $SCRIPTFOLDER/zenoh_config_zeppelin.json:/zenoh_config_zeppelin.json \
  -v $SCRIPTFOLDER/zenoh_config_links_guest.json:/zenoh_config_links_guest.json \
  -v $SCRIPTFOLDER/zenoh_config_test_template.json:/zenoh_config_testzep.json \
  --entrypoint "/entrypoint.sh" \
  eclipse/zenoh-bridge-ros2dds:1.8.0
