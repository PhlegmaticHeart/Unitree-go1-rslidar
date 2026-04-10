from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterFile
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

package_name = 'helios16p_cane_robot'



def generate_launch_description():


# ----------------------------------- Files' path retrieval -----------------------------------

    pkg_share = FindPackageShare('helios16p_cane_robot').find('helios16p_cane_robot') # Package share directory

    bag_path = '' # Bag file path
   
# ----------------------------------- Simulation and bag flags parameters -----------------------------------

    declare_simulate_arg = DeclareLaunchArgument(
        'simulate',
        default_value='True',
        description='Flag simulation time + bag'
    )
    simulate = LaunchConfiguration('simulate') # Flag simulation time + bag

    declare_use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value=simulate,
        description='Flag to enable simulation time'
    )
    use_sim_time = LaunchConfiguration('use_sim_time') # Flag to enable simulation time


    declare_play_bag_arg = DeclareLaunchArgument(
        'play_bag',
        default_value=simulate,
        description='Flag to enable bag file playback'
    )
    play_bag = LaunchConfiguration('play_bag')  # Flag to enable bag file playback

    declare_bagfile_arg = DeclareLaunchArgument(
        'bagfile',
        default_value=bag_path,
        description='Path to the bag file'
    )
    bagfile = LaunchConfiguration('bagfile') # Bag file path

    declare_nomap_arg = DeclareLaunchArgument(
        'nomap',
        default_value='False',
        description='Flag to disable map->odom transform for better performance evaluation of kiss-ICP'
    )
    nomap = LaunchConfiguration('nomap') # Flag to disable map->odom

# ----------------------------------- Kiss-ICP's debug parameters -----------------------------------

    declare_visualize_clouds_arg = DeclareLaunchArgument(
        'visualize_clouds',
        default_value='True',
        description='Flag to enable rviz visualization of clouds published by kiss-ICP'
    )
    visualize_clouds = LaunchConfiguration('visualize_clouds') # Flag to enable rviz visualization of clouds published by kiss-ICP

    declare_base_frame_arg = DeclareLaunchArgument(
        'base_frame',
        default_value='base_link',
        description='Base frame for the robot'
    )
    base_frame = LaunchConfiguration('base_frame')  # (base_link/base_footprint)

    declare_odom_frame_arg = DeclareLaunchArgument(
        'odom_frame',
        default_value='odom',
        description='Name of the lidar odometry frame'
    )
    odom_frame = LaunchConfiguration('odom_frame') # It gives the name to the frame of the odometry published by kiss-ICP


    declare_publish_odom_tf_arg = DeclareLaunchArgument(
        'publish_odom_tf',
        default_value='True',
        description='Flag to publish odom->base_link transform'
    )
    publish_odom_tf = LaunchConfiguration('publish_odom_tf') # Flag to publish odom->base_link transform


    declare_invert_odom_tf_arg = DeclareLaunchArgument(
        'invert_odom_tf',
        default_value='False',
        description='Flag to invert the odometry transform'
    )
    invert_odom_tf = LaunchConfiguration('invert_odom_tf') # necessary for getting the correct transform as by default kiss-ICP pblishes an inverted transform


    declare_nokiss_arg = DeclareLaunchArgument(
        'nokiss',
        default_value='False',
        description='Flag to disable kiss-ICP'
    )
    nokiss = LaunchConfiguration('nokiss') # Flag to enable rviz visualization


    declare_kiss_config_name_arg = DeclareLaunchArgument(
        'setrange',
        default_value='lidar_config_mr8.yaml',
        description='Name of kiss-icp yaml configuration to load'
    )
    kiss_config_name = LaunchConfiguration('setrange') # Configuration file name to load, by default its set to 100m range


    kiss_config_name_path = PathJoinSubstitution([
        FindPackageShare(package_name),
        'configs',
        kiss_config_name
    ])
# ----------------------------------- Topics' configuration -----------------------------------

    declare_topic_arg = DeclareLaunchArgument(
        'topic',
        default_value='/rslidar_points',   # Driver's topic
        description='Input pointcloud topic for KISS-ICP'
    )
    pointcloud_topic = LaunchConfiguration('topic')


# ----------------------------------- Nodes -----------------------------------

    tf2_map_to_odom = Node( # Static transform from map to base_frame
            package='tf2_ros',
            name='static_transform_map_to_odom',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', odom_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
            condition=UnlessCondition(nomap)
        )


    tf2_base_frame_to_rslidar = Node( # Static transform from base_frame to rslidar
            package='tf2_ros',
            name='static_transform_base_frame_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', base_frame, 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    bag_start_process = ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play',
                bagfile,  
                '--topics', '/rslidar_points', 
                '--rate', '1.0',
                '--clock', '1.0'
            ],
            output='screen',
            condition=IfCondition(play_bag),
            name='startmybag'
        )


    kiss_node = Node( # kiss-ICP node
            package='kiss_icp',
            executable='kiss_icp_node',
            name='kiss_icp_node',
            output='screen',
            remappings=[
                ('pointcloud_topic', pointcloud_topic),
            ],
            parameters=[
                ParameterFile(kiss_config_name_path),# Load the configuration file, by default its the 100m range one

                #///kiss-ICP's configuration\\\
                {

                'publish_debug_clouds': visualize_clouds, # Toggle rviz visualization
                'use_sim_time': use_sim_time,      # Toggle simulation time
                'base_frame': base_frame,
                'publish_odom_tf': publish_odom_tf,
                'invert_odom_tf': invert_odom_tf,
                'lidar_odom_frame': odom_frame,

                },
            ],
            condition=UnlessCondition(nokiss)
        )

# ----------------------------------- Nodes and commands execution -----------------------------------

    return LaunchDescription([

        declare_simulate_arg,
        declare_use_sim_time_arg,
        declare_play_bag_arg,
        declare_bagfile_arg, 
        declare_nomap_arg,  
        declare_visualize_clouds_arg,
        declare_nokiss_arg,
        declare_base_frame_arg,
        declare_odom_frame_arg,
        declare_publish_odom_tf_arg,
        declare_invert_odom_tf_arg,
        declare_topic_arg,
        declare_kiss_config_name_arg,

        tf2_map_to_odom,
        tf2_base_frame_to_rslidar,
        kiss_node,
        bag_start_process,

    ]   
)
