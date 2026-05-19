#!/bin/bash


set -e

IMAGE_NAME="rosnav2_cyclone"
TAG="latest"
PLATFORM=$(docker info --format '{{.Architecture}}')  # Auto-detect

echo "Starting $IMAGE_NAME"
docker run \
  --rm \
  -it \
  --name rosnav_cyclone_container \
  --privileged \
  --network=host \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/.Xauthority:/root/.Xauthority \
  -v /home/$USER:/home/admin/bench \
  -v ./nav2_params.yaml:/home/admin/nav2_params.yaml \
  -v ./cyclonedds_config.xml:/cyclonedds_config.xml \
  -v ./entrypoint.sh:/entrypoint.sh \
  -v ./nav2_params.yaml:/home/admin/nav2_params.yaml \
  -v ./maps:/home/admin/maps \
  -v ./ros_utilities:/home/admin/ros_utilities \
  -v ./custom_navigate_to_pose_w_replanning_and_recovery.xml:/home/admin/custom_navigate_to_pose_w_replanning_and_recovery.xml \
  -e DISPLAY=$DISPLAY \
  -e XAUTHORITY=/root/.Xauthority \
  -e ROS_DOMAIN_ID=7 \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
  -e CYCLONEDDS_URI=/cyclonedds_config.xml \
  -e ROS_DISTRO=humble \
  -e ROS_LOCALHOST_ONLY=1 \
  --entrypoint /entrypoint.sh \
  "$IMAGE_NAME:$TAG"
