#!/bin/bash



echo "#DOUBLE ROSE" >> ~/.bashrc
echo "alias editbashrc='nano ~/.bashrc'" >> ~/.bashrc
echo "alias sourcebashrc='source ~/.bashrc'" >> ~/.bashrc
echo "#DOUBLE ROSE" >> ~/.bashrc
echo "alias rosframe='ros2 run tf2_tools view_frames -o temp_frame && xdg-open temp_frame.pdf'" >> ~/.bashrc
echo "alias sourceros2='source /opt/ros/humble/setup.bash'" >> ~/.bashrc
echo "alias sourceinst='source install/setup.bash'" >> ~/.bashrc
echo "alias rostfstatica='ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0'" >> ~/.bashrc

echo "alias killred='sudo pkill ros-* && pkill ros_* && pkill ros/*'" >> ~/.bashrc

echo "alias rosnav_bringup='ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/admin/maps/ufficio/map.yaml params_file:=/home/admin/nav2_params.yaml'" >> ~/.bashrc
echo "alias rosnav_rviz='ros2 run rviz2 rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz'" >> ~/.bashrc


echo "alias rosmap1nav='ros2 launch nav2_bringup navigation_launch.py'" >> ~/.bashrc
echo "alias rosmap2slam='ros2 launch slam_toolbox online_async_launch.py'" >> ~/.bashrc

#ssh

echo "alias jumpuni='ssh -Y -J pi@192.168.50.133 unitree@192.168.123.15'" >> ~/.bashrc
echo "alias sshpi_zep='ssh -Y pi@192.168.50.133'" >> ~/.bashrc
echo "alias sshpi_lg='ssh -Y pi@172.30.231.133'" >> ~/.bashrc
echo "alias sshubu='ssh -Y ubuntu@192.168.50.244'" >> ~/.bashrc
echo "alias sshxav='ssh -Y unitree@192.168.50.148'" >> ~/.bashrc

echo "alias autorestartzenohhelio_zeppelin='ssh pi@192.168.50.133 "/opt/custom_scripts/zenoh_REBOOT.sh"'" >> ~/.bashrc
echo "alias autorestartzenohhelio_lg='ssh pi@172.30.231.133 "/opt/custom_scripts/zenoh_REBOOT.sh"'" >> ~/.bashrc
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source /home/admin/ros_utilities/install/setup.bash" >> ~/.bashrc

echo "alias rosnav_navigation='ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/admin/maps/ufficio/map.yaml params_file:=/home/admin/nav2_params.yaml'" >> ~/.bashrc
echo "alias rosnav_start_mapping='ros2 run slam_toolbox async_slam_toolbox_node --ros-args --params-file /home/admin/ros_utilities/src/nav2_wrapper/configs/slam_toolbox.yaml'" >> ~/.bashrc
echo "alias rosnav_save_map_as='ros2 run nav2_map_server map_saver_cli -f'" >> ~/.bashrc

exec /bin/bash
