#!/bin/bash

exec bash -c "source /opt/ros/humble/setup.bash && source helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py"
