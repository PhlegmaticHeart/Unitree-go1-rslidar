#!/bin/bash

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=/cyclonedds_config.xml 

bash -c "source /home/admin/.bashrc && source /opt/ros/humble/setup.bash && source /home/admin/helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py setrange:=mrange8.yaml visualize_clouds:=true nomap:=true state_publisher:=false"
