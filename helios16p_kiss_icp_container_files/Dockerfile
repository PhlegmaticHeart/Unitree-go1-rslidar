#FROM osrf/ros:humble-desktop-jammy
FROM ros:humble-ros-base@sha256:370191995451bb63f2e37bb2f6636a09f66ca810d0865703058361dc6ac70c87

#Avoid interactive mode during installation
ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -ms /bin/bash admin

RUN usermod -aG sudo admin

# Installs necessary tools
RUN apt-get update && apt install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

# Creates and set directory workspace
WORKDIR /home/admin/helios16p_ws
RUN mkdir -p src

# Copy the ROS packages
COPY helios16p_ws/src/ src/

# ROS dependencies installation, necessary to packages build
RUN apt-get update && apt install -y libpcap-dev \
    libeigen3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y \
    || echo "Some rosdep packages failed, install them manually"

RUN apt-get update && apt-get install -y \
    ros-humble-ament-cmake \
    && rm -rf /var/lib/apt/lists/* \
    && . /opt/ros/humble/setup.sh

# Entrypoint configuration for ROS and source of workspace's setup.bash
RUN echo "source /opt/ros/humble/setup.bash" > /ros_entrypoint.sh \
    && echo "source /home/admin/helios16p_ws/install/setup.bash" >> /ros_entrypoint.sh \
    && echo "exec \"\$@\"" >> /ros_entrypoint.sh \
    && chmod +x /ros_entrypoint.sh
    
# Get cyclone-dds and copy the relative xml config file - If you want to use eprosima fast dds, comment the next RUN and COPY
RUN apt-get update && apt-get install -y ros-humble-rmw-cyclonedds-cpp
COPY cyclonedds_config.xml /

# Get rviz2, vim
RUN apt-get update && apt install -y libxcb-cursor0 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 ros-humble-rviz2 vim

# Installs all required python packages
RUN apt-get update && apt-get install -y pip
RUN pip install cmake xacro

# Export CMAKE_POLICY_VERSION_MINIMUM to 3.5, because Kiss-ICP build needs cmake 3.24
ENV CMAKE_POLICY_VERSION_MINIMUM=3.10

# Ulteriori librerie necessarie
RUN apt-get update && apt-get install -y libpcap-dev

# Build workspace
RUN . /opt/ros/humble/setup.sh && \ 
    colcon build --packages-select rslidar_msg --symlink-install && colcon build --packages-skip rslidar_msg

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

# Copy the entrypoint and manage its permissions
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Change user to admin and workdir to /home/admin
USER admin

WORKDIR /home/admin

# Aliases
RUN echo "alias start='source /home/admin/helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py setrange:=mrange8.yaml visualize_clouds:=true'" >> ~/.bashrc

# Automatical source - If you want to use eprosima fast dds, comment the last two echoes
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "source ~/helios16p_ws/install/setup.bash" >> ~/.bashrc \
    && echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc \
    && echo 'export CYCLONEDDS_URI=/cyclonedds_config.xml' >> ~/.bashrc 
 
RUN bash -c 'source ~/.bashrc'

# Entrypoint setup
#ENTRYPOINT ["/bin/bash"] uncomment if you want to use the container interactively and then comment the following entrypoint

ENTRYPOINT ["/entrypoint.sh"]


