set -e

IMAGE_NAME="helios16p_kiss-icp_cyclone"
TAG="latest"
SCRIPTFOLDER=$( dirname $0 )

echo "Starting $IMAGE_NAME"

docker run \
  --rm \
  -it \
  --privileged \
  --network=host \
  --name helios16_kiss-icp_container \
  -e DISPLAY=$DISPLAY \
  -e XAUTHORITY=/root/.Xauthority \
  -e ROS_DOMAIN_ID=3 \
  -e CYCLONEDDS_URI=/cyclonedds_config.xml \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
  -e ROS_DISTRO=humble \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/.Xauthority:/root/.Xauthority \
  -v $SCRIPTFOLDER/entrypoint.sh:/entrypoint.sh \
  -v $SCRIPTFOLDER/cyclonedds_config.xml:/cyclonedds_config.xml \
  -v $SCRIPTFOLDER/helios16p_ws:/home/admin/debug_build \
  --entrypoint /entrypoint.sh \
  "$IMAGE_NAME:$TAG"

