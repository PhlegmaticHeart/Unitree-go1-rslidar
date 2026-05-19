#FROM osrf/ros:humble-desktop-jammy
FROM ros:humble-ros-base

#Avoid interactive mode during installation
ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN useradd -ms /bin/bash admin

RUN usermod -aG sudo admin

# Installs necessary tools
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

# ROS desktop update
RUN apt-get update && apt-get install -y  ros-humble-desktop \
    ros-dev-tools \
    ros-build-essential


# ROS dependencies installation, necessary to packages build
RUN apt-get update && apt-get install -y libpcap-dev libeigen3-dev \
    && rm -rf /var/lib/apt/lists/* 

RUN apt-get update && apt-get install -y \
    ros-humble-ament-cmake \
    && rm -rf /var/lib/apt/lists/* \
    && . /opt/ros/humble/setup.sh

# Initialize rosdep, you have to update at runtime as update cache won't be kept
RUN rosdep init || true

#get rviz2, nano
RUN apt-get update && apt-get install -y ros-humble-rviz2 nano

# Update to cmake 4.20
RUN apt-get update && apt-get install -y pip && pip install cmake xacro

# Export CMAKE_POLICY_VERSION_MINIMUM to 3.5, because Kiss-ICP build needs cmake 3.24
ENV CMAKE_POLICY_VERSION_MINIMUM=3.5

# Get cyclone-dds
RUN apt-get update && apt-get install -y ros-humble-rmw-cyclonedds-cpp

# Copy the cyclone-dds xml config file
COPY cyclonedds_config.xml /

# Gets nav2 bringup
RUN apt-get update && apt-get install -y \
    ros-humble-navigation2 ros-humble-nav2-bringup

RUN apt-get update && apt-get install -y \
    ros-humble-nav2-route

# QOF packages

RUN apt-get update \ 
    && apt-get install -y \
    ros-humble-teleop-twist-keyboard \
    && rm -rf /var/lib/apt/lists/*









# If no password is needed, then uncomment this line and comment the following two lines 
#RUN echo "root ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN --mount=type=secret,id=pusrs \
    echo "root:$(sed -n '1s/\s*#.*$//p' /run/secrets/pusrs)" | chpasswd

#If no password is needed, then uncomment this line and comment the following two lines
#RUN echo "admin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN --mount=type=secret,id=pusrs \
    echo "admin:$(sed -n '2s/\s*#.*$//p' /run/secrets/pusrs)" | chpasswd

#this is the template if you want to add a third user, if you want to add more users, remember to change the sed command selected output line accordingly 
#RUN --mount=type=secret,id=root \
#   echo "MY_USER:$(sed -n '3s/\s*#.*$//p' /run/secrets/proot)" | chpasswd


COPY entrypoint.sh /home/admin

RUN chmod +x /home/admin/entrypoint.sh

# Chnge user to admin and workdir to /home/admin
USER admin

WORKDIR /home/admin
    
RUN bash -c 'source ~/.bashrc'

ENTRYPOINT ["/home/admin/entrypoint.sh"]


