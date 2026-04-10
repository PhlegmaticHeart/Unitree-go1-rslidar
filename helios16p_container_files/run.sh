set -e

IMAGE_NAME="helios16p_kiss-icp_cyclone"
TAG="latest"

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
  -e ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/.Xauthority:/root/.Xauthority \
  --mount type=bind,source=./entrypoint.sh,target=/usr/bin/entrypoint.sh \
  --mount type=bind,source=./helios16p_ws,target=/home/admin/debug_build \
  --entrypoint /usr/bin/entrypoint.sh \
  "$IMAGE_NAME:$TAG"

