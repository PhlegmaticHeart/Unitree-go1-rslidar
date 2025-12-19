![Logo](Unitree-go1-rslidar/blob/main/assets/links_its.png))

# Workspace for out-of-the-box Helios 16 P Deploy

///This project aims to integrate the Robosense Helios 16 P on a robot dog\\\

§

Actually, the folder of interest for getting a working kiss_icp pipeline setup is helios16p_ws.
Folder tutorial_wss is a group of workspaces made to better undestand how ROS 2 works.

______________________________________________________________________________________________________________________											

<span style='color: red;'>long</span>

## § Workspace structure §

In the helios16p_ws workspaces there are the following packages:

rslidar_msg

rslidar_sdk

kiss_icp

helios16p_cane_robot

______________________________________________________________________________________________________________________

## § Packages functions §

rslidar_msg: Contains the msg structure that rslidar_sdk expects.

rslidar_sdk: Contains the drivers of Helios 16 P lidar, they are handled by the node rslidar_sdk_node.

kiss_icp: Contains the odometry SLAM pipeline with a personalized configuration of Rviz for a better visualization of the ongoing matters.

helios16p_cane_robot: Contains a launch file and an urdf model with xacro syntax, be sure to install xacro throught pip before attempting to load it. 
                      With the growth of the project, the urdf will become more complex and eventually will comprehend an entire model of the robot dog.

______________________________________________________________________________________________________________________

## § Launch file parameters §

The launch file actually has the following parameters: 

- simulate:=True/False -> its a flag to enable or disable the simulated environment, to enable it you first require a ros bag.
                          Its set by default to false.

- bagfile:='<your/bag/path>' -> it allows you to set a different path for your bag file.

- visualize:=True/False -> it enables Rviz visualization, its False by default and its recommended so for containerization.

- max_range:=<double> ->

- min_range:=<double> ->

- mapping_voxel_size:=<double> ->

- mapping_voxel_points:=<double> ->

- data_deskew:=True/False ->

- base_frame:=True/False ->

- lidar_odom_frame:=<double> ->

- publish_odom_tf:=True/False ->

- invert_odom_tf:=True/False ->

- position_covariance:=<double> ->

- orientation_covariance:=<double> ->

- max_num_iterations:=<int> ->

- convergence_criterion:=<float> ->

Their default values can be set in the launch file's def generate_launch_description.
These parameters are included exclusively for debugging and testing.

If you want to load a certain configuration, please,
change the **default_config_file_path** variable path or load it with **ros2 param load <file_path>* .

______________________________________________________________________________________________________________________

## § Launch description §
 
The launch file actually contains the following nodes:

**NODE** | robot_state_publisher: Displays the urdf, accordingly to frames.

**NODE** | static_transform_map_to_base_link: Powered by tf2,
		   sends the static transform of the map topic to the base_link topic (to tell the base link that its location is based upon the map).

**NODE** | static_transform_base_link_to_rslidar: Powered by tf2, 
           sends the static transform of the base_link topic to the rslidar topic (to tell the rslidar that it must be fixed to its base).

**PROCESS** | startmybag: Its a ROS 2 command that start a bag loop, 
              with the correct time clock to prevent simulation blockage due to incorrect datastamps.
              Note: This process will be executed only if the simulation flag is set true.

**NODE** | rslidar_sdk: Starts the driver handler, opening the topic rslidar_points where lidar data will be received.
         **Note:* This process will be executed only if the simulation flag is set false.

**NODE** | kiss_icp: Starts the pipeline for converting lidar data to odometry.

**NODE** | rviz2: Starts a preconfigured, working out of the box rviz2 session,
           equipped with visual data, visual odometry and visual mapping.

______________________________________________________________________________________________________________________

## § Behaviour §

If simulate is flagged true:

- The lidar drivers handler node won't start.

- The ROS bag you specified will be loop-played, with a fake clock for your rviz2 session.

- Kiss_icp pipeline will start running, sending odometry data to /kiss/pose topic.

- The rviz2 session will start with a custom config file and it'll show the raw data visualization with a odometry and mapped data output as well.


if simulate is flagged false:

- The lidar drivers handler node will start.

- The ROS bag you specified will be ignored.

- Kiss_icp pipeline will start running, sending odometry data to /kiss/pose topic.

- The rviz2 session will start with a custom config file and it'll show the raw data visualization with a odometry and mapped data output as well.

______________________________________________________________________________________________________________________

## § Building §

Its necessary, if building from scratch is needed, to build rslidar_msg package BEFORE rslidar_sdk, as its required by the latter to build effectively.

______________________________________________________________________________________________________________________

## § Next steps §

Soon there will be:

- a multi-architecture docker container image linked to this page, with, for completion, a Dockerfile to let you tune the application.

- a benchmark of the Kiss-ICP pipeline respect to a Vicon based groundtruth.
  
______________________________________________________________________________________________________________________

## § Infos on the project §

This project is currently a cooperational project led by Links Foundation and ITS Meccatronica e Aerospazio Piemonte (MAP).




