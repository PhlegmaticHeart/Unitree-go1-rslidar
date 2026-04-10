#!/bin/bash

# Aliases
echo "alias start='source /home/admin/helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16_cane_robot.launch.py setrange:=mrange8.yaml'" >> ~/.bashrc

# Automatical source - If you want to use eprosima fast dds, comment the last two echoes
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
  && echo "source ~/helios16p_ws/install/setup.bash" >> ~/.bashrc \
  && echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc \
  && echo 'export CYCLONEDDS_URI=/cyclonedds_config.xml' >> ~/.bashrc

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=/cyclonedds_config.xml 

bash -c "source /home/admin/.bashrc && source /opt/ros/humble/setup.bash && source /home/admin/helios16p_ws/install/setup.bash && ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py setrange:=mrange8.yaml"
