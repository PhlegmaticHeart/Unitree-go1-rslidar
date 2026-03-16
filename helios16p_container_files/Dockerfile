FROM ros:humble-ros-base@sha256:370191995451bb63f2e37bb2f6636a09f66ca810d0865703058361dc6ac70c87

#Avoid interactive mode during installation
ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -ms /bin/bash admin

RUN usermod -aG sudo admin

# Creates and set directory workspace
WORKDIR /home/admin/helios16p_ws
RUN mkdir -p src

# Copy the ROS packages, comment those that you don't need

COPY helios16p_ws/src/rslidar_msg/ src/rslidar_msg/
COPY helios16p_ws/src/rslidar_sdk/ src/rslidar_sdk/

COPY helios16p_ws/src/kiss-icp/ src/kiss-icp/
COPY helios16p_ws/src/helios16p_cane_robot/ src/helios16p_cane_robot/
COPY helios16p_ws/src/pointcloud_to_laserscan/ src/pointcloud_to_laserscan/

COPY helios16p_ws/src/vicon_receiver/ src/vicon_receiver/
COPY helios16p_ws/src/go1_description/ src/go1_description/

COPY helios16p_ws/src/ros2_unitree_legged_msgs/ src/ros2_unitree_legged_msgs/
COPY helios16p_ws/src/unitree_legged_real/ src/unitree_legged_real/
COPY helios16p_ws/src/unitree_nav/ src/unitree_nav/
COPY helios16p_ws/src/unitree_nav_interfaces/ src/unitree_nav_interfaces/
COPY helios16p_ws/src/cloudini_ros/ src/cloudini_ros/

# Installs necessary tools
RUN apt-get update && apt install -y \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

# ROS dependencies installation, necessary to packages build
RUN apt-get update && apt install -y libpcap-dev \
    libeigen3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    ros-humble-ament-cmake \
    && rm -rf /var/lib/apt/lists/* \
    && . /opt/ros/humble/setup.sh

# Get cyclone-dds and copy the relative xml config file - If you want to use eprosima fast dds, comment the next RUN and COPY
RUN apt-get update && apt-get install -y ros-humble-rmw-cyclonedds-cpp
COPY cyclonedds_config.xml /

# Get rviz2, vim - Just for debuggin, comment if you dont need them
RUN apt-get update && apt install -y libxcb-cursor0 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 ros-humble-rviz2 vim \
    && rm -rf /var/lib/apt/lists/*

# Installs all required python packages
RUN apt-get update && apt-get install -y pip
RUN pip install cmake xacro

# Export CMAKE_POLICY_VERSION_MINIMUM to 3.10, because Kiss-ICP build needs cmake 3.24
ENV CMAKE_POLICY_VERSION_MINIMUM=3.10

# Other requirements
RUN apt-get update && apt-get install -y libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

# Requirements for Uinitree Legged packages - BEGINNING (comment up to the END if you don't need the unitree legged package)
RUN sudo apt-get update
RUN apt-get install -y libboost-dev
RUN apt-get install -y libglib2.0-dev
RUN yes | apt-get -y install unzip
RUN yes | apt-get -y install openjdk-8-jdk
RUN rm -rf /var/lib/apt/lists/*

# run sudo update-alternatives --config javac
# and choose java-8-openjdk (here option 2)
RUN echo 2 | update-alternatives --config javac

# install LCM
WORKDIR /lcm
RUN curl -O -L https://github.com/lcm-proj/lcm/releases/download/v1.4.0/lcm-1.4.0.zip
RUN unzip -q lcm-1.4.0.zip && cd lcm-1.4.0 && mkdir build && cd build && cmake .. && make && sudo make install
RUN ldconfig -v
# revert to java-11-openjdk (here option 0)
RUN echo 0 | update-alternatives --config javac

# Requirements for Uinitree Legged packages - END




# Build workspace
WORKDIR /home/admin/helios16p_ws

RUN apt-get update && apt-get install -y ca-certificates
RUN rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y
#    || echo "Some rosdep packages failed, install them manually"

RUN . /opt/ros/humble/setup.sh && \
    colcon build --packages-select rslidar_msg ros2_unitree_legged_msgs unitree_nav_interfaces --symlink-install \
    && colcon build --packages-skip rslidar_msg ros2_unitree_legged_msgs --symlink-install

# If no password is needed, then uncomment this line and comment the following two lines 
#RUN echo "root ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN --mount=type=secret,id=pusrs \
    echo "root:$(sed -n '1s/\s*#.*$//p' /run/secrets/pusrs)" | chpasswd

#If no password is needed, then uncomment this line and comment the following two lines
#RUN echo "admin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN --mount=type=secret,id=pusrs \
    echo "admin:$(sed -n '2s/\s*#.*$//p' /run/secrets/pusrs)" | chpasswd

#this is the template if you want to add a third user, if you want to add more users, remember to change the sed command selected output line accordingly 
#RUN --mount=type=secret,id=pusrs \
#   echo "MY_USER:$(sed -n '3s/\s*#.*$//p' /run/secrets/proot)" | chpasswd

# Copy the entrypoint and manage its permissions
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Change user to admin and workdir to /home/admin
USER admin

WORKDIR /home/admin

# Aliases
RUN echo "alias start='source /home/admin/helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py setrange:=mrange8.yaml'" >> ~/.bashrc

# Automatical source - If you want to use eprosima fast dds, comment the last two echoes
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "source ~/helios16p_ws/install/setup.bash" >> ~/.bashrc \
    && echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc \
    && echo 'export CYCLONEDDS_URI=/cyclonedds_config.xml' >> ~/.bashrc

RUN bash -c 'source ~/.bashrc'

# Entrypoint setup
#ENTRYPOINT ["/bin/bash"] uncomment if you want to use the container interactively and then comment the following entrypoint

ENTRYPOINT ["/entrypoint.sh"]