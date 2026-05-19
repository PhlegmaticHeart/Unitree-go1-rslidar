#FROM osrf/ros:debian-boo
FROM eclipse/zenoh-bridge-ros2dds:1.8.0

#Avoid interactive mode during installation
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

# Entrypoint
RUN rm entrypoint.sh
COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

# Config file for zenoh
COPY zenoh_config.json /

#cyclone config file
COPY cyclonedds_config.xml /

ENTRYPOINT ["/entrypoint.sh"]


