///This project aims to integrate the Robosense Helios 16 P) on a robot dog\\\

Actually, the folder of interest is helios16p_ws.
Folder tutorial_wss is a group of workspaces made to better undestand how ROS 2 works.

###########################################################################################

In the helios16p_ws workspaces there are the following packages:

rslidar_msg

rslidar_sdk

kiss_icp

helios16p_cane_robot

###########################################################################################

§ Packages functions §

rslidar_msg: Contains the msg structure that rslidar_sdk expects.

rslidar_sdk: Contains the drivers of Helios 16 P lidar, they are handled by the node rslidar_sdk_node.

kiss_icp: Contains the odometry SLAM pipeline with a personalized configuration of Rviz for a better visualization of the ongoing matters.

helios16p_cane_robot: Contains a launch and an urdf model. 
With the growth of the project, it'll become more complex and eventually will comprehend and entire model of the robot dog.


###########################################################################################

§ Launch file parameters §

The launch file actually has the following parameters:

simulation:=true/false -> its a flag to enable or disable the simulated environment, to enable it you first require a ros bag.
Its set by default to false.

bagfile:='<your/bag/path>' -> it allow you to set a different path for your bag file.
Its default value can be set in the launch file's def generate_launch_description.

§ Launch description §
 
The launch file actually contains the following nodes:

NODE | robot_state_publisher: Displays the urdf, accordingly to frames.

NODE | static_transform_map_to_base_link: Powered by tf2,
sends the static transform of the map topic to the base_link topic (to tell the base link that its location is based upon the map).

NODE | static_transform_base_link_to_rslidar: Powered by tf2, 
sends the static transform of the base_link topic to the rslidar topic (to tell the rslidar that it must be fixed to its base).

PROCESS | startmybag: Its a ROS 2 command that start a bag loop, 
with the correct time clock to prevent simulation blockage due to incorrect datastamps.
Note: This process will be executed only if the simulation flag is set true.

NODE | rslidar_sdk: Starts the driver handler, opening the topic rslidar_points where lidar data will be received.
Note: This process will be executed only if the simulation flag is set false.

NODE | kiss_icp: Starts the pipeline for converting lidar data to odometry.

NODE | rviz2: Starts a preconfigured, working out of the box rviz2 session,
equipped with visual data, visual odometry and visual mapping.


