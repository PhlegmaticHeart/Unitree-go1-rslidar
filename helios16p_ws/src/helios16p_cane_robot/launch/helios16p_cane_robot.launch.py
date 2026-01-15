from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
import xacro
import os

package_name = 'helios16p_cane_robot'

def generate_launch_description():

# Files' path retrieval
    pkg_share = FindPackageShare('helios16p_cane_robot').find('helios16p_cane_robot') # Package share directory

    default_config_file_path = os.path.join( # Default Kiss-ICPconfiguration file path
        get_package_share_directory(package_name), 'configs', 'config_mrange100_voxsize5Em1_voxpoints20.yaml'
    )
    
    custom_config_file_path = os.path.join( # Custom configuration file path
        get_package_share_directory(package_name), 'configs', 'config_mrange30_voxsize3Em1_voxpoints10.yaml'
    )

    xacro_file = os.path.join(pkg_share, 'urdf', 'helios16p.urdf.xacro') # Robot's xacro file path
    robot_description = xacro.process_file(xacro_file).toxml() # Robot description in xml format, keep in mind that this model requires xacro package

    lidar_config_file = os.path.join(pkg_share, 'configs', 'lidar_config.yaml') # RSLidar's config file path

    bag_path = '/home/ph/bagrecords/bagtest600/rosbag2_600_BIG/' # Bag file path

# Simulation and bag flags
    simulate = LaunchConfiguration('simulate', default=False) # Flag simulation time + bag
    use_sim_time = LaunchConfiguration('use_sim_time', default=simulate) # Flag to enable simulation time
    play_bag = LaunchConfiguration('play_bag', default=simulate)  # Flag to enable bag file playback
    bagfile = LaunchConfiguration('bagfile', default=bag_path) # Bag file path

# Kiss-ICP's debug parameters
    visualize = LaunchConfiguration('visualize', default=False) # Flag to enable rviz visualization
    max_range = LaunchConfiguration('data.max_range', default=30.0) # By default its 100
    min_range = LaunchConfiguration('data.min_range', default=0.2) # By default its 0
    mapping_voxel_size = LaunchConfiguration('mapping.voxel_size', default=0.3) # By default its 0.5
    mapping_voxel_points = LaunchConfiguration('mapping.max_points_per_voxel', default=10) # By default its 20
    data_deskew = LaunchConfiguration('data.deskew', default=True) # Enable manipulation of max and min range
    base_frame = LaunchConfiguration('base_frame', default='')  # (base_link/base_footprint)
    lidar_odom_frame = LaunchConfiguration('lidar_odom_frame', default='odom_lidar') # It gives the name to the frame of the odometry published by kiss-ICP
    publish_odom_tf = LaunchConfiguration('publish_odom_tf', default=True) # Flag to publish odom->base_link transform
    invert_odom_tf = LaunchConfiguration('invert_odom_tf', default=True) # necessary for getting the correct transform as by default kiss-ICP pblishes an inverted transform
    max_num_iterations = LaunchConfiguration('registration.max_num_iterations', default=700) # By default its 500
    convergence_criterion = LaunchConfiguration('registration.convergence_criterion', default=0.000001) # By default its 0.0001

# Topics' configuration
    declare_topic_arg = DeclareLaunchArgument(
        'topic',
        default_value='/rslidar_points',   # Driver's topic
        description='Input pointcloud topic for KISS-ICP'
    )
    pointcloud_topic = LaunchConfiguration('topic')

# Nodes and commands execution
    return LaunchDescription([

        declare_topic_arg,

        Node( # Publish robot state
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': use_sim_time,
            }],
        ),
        Node( # Static transform from map to base_link
            package='tf2_ros',
            name='static_transform_map_to_base_link',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
        ),
        Node( # Static transform from base_link to rslidar
            package='tf2_ros',
            name='static_transform_base_link_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
        ),

        ExecuteProcess( # Bag file playback
            cmd=[
                'ros2', 'bag', 'play',
                '--rate', '0.5',
                bagfile,
                '--clock', '0.5', '--loop',
                '--topic', '/rslidar_points',
            ],
            output='screen',
            condition=IfCondition(play_bag),
            name='startmybag',
        ),

        Node( # Driver node
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios16p_node',
            output='screen',
            parameters=[{'config_path': lidar_config_file}],
            condition=UnlessCondition(play_bag),
        ),

        Node( # kiss-ICP node
            package='kiss_icp',
            executable='kiss_icp_node',
            name='kiss_icp_node',
            output='screen',
            remappings=[
                ('pointcloud_topic', pointcloud_topic),
        ],
            parameters=[


            default_config_file_path,   #
                                        # Main configurations, just de-flag the desired one and flag the other
            #custom_config_file_path,   #


                {#///kiss-ICP's configuration\\\

                 'publish_debug_clouds': visualize, # Toggle rviz visualization
                 'use_sim_time': use_sim_time,      # Toggle simulation time
                 'base_frame': base_frame,
                 'publish_odom_tf': publish_odom_tf,
                 'invert_odom_tf': invert_odom_tf,
                 'lidar_odom_frame': lidar_odom_frame,
                 'data.deskew': data_deskew,

                # Main parameters to tune for performance evaluation

                 'data.max_range': max_range,
                 'data.min_range': min_range,
                 'mapping.max_points_per_voxel': mapping_voxel_points,
                 'mapping.voxel_size': mapping_voxel_size,
                 'registration.convergence_criterion': convergence_criterion,
                 'registration.max_num_iterations': max_num_iterations,

                # More parameters available for tuning in the configuration files

                 #'adaptive_threshold.initial_threshold',
                 #'adaptive_threshold.min_motion_th',
                 #'registration.max_num_threads':,
                 #'orientation_covariance': orientation_covariance,
                 #'position_covariance': position_covariance,
                },
            ],
        ),


        Node( # Rviz2 node
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=[
                '-d',
                PathJoinSubstitution([FindPackageShare('kiss_icp'), 'rviz', 'kiss_icp.rviz']),
            ],
            parameters=[{'use_sim_time' : use_sim_time}],
            condition=IfCondition(visualize),
    )
    ])
