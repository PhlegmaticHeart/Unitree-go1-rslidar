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
    pkg_share = FindPackageShare('helios16p_cane_robot').find('helios16p_cane_robot')

    default_config_file_path = os.path.join(
        get_package_share_directory(package_name), 'configs', 'config.yaml'
    )

    custom_config_file_path = os.path.join(
        get_package_share_directory(package_name), 'configs', 'config_mrange25_voxsize3Em1_voxpoints10.yaml'
    )    

    xacro_file = os.path.join(pkg_share, 'urdf', 'helios16p.urdf.xacro')
    robot_description = xacro.process_file(xacro_file).toxml()
    
    lidar_config_file = os.path.join(pkg_share, 'configs', 'lidar_config.yaml')

    bag_path = '/home/ph/bagrecords/bagtest600/rosbag2_600_BIG/'

# Simulation and bag flags
    simulate = LaunchConfiguration('simulate', default=False) # Flag simulation time + bag
    use_sim_time = LaunchConfiguration('use_sim_time', default=simulate) # Flag to enable simulation time
    play_bag = LaunchConfiguration('play_bag', default=simulate)  # Flag to enable bag file playback
    bagfile = LaunchConfiguration('bagfile', default=bag_path) # Bag file path

# Kiss-ICP's debug parameters    
    visualize = LaunchConfiguration('visualize', default=False)
    max_range = LaunchConfiguration('data.max_range', default=30.0) # By default its 100
    min_range = LaunchConfiguration('data.min_range', default=0.2) # By default its 0
    mapping_voxel_size = LaunchConfiguration('mapping.voxel_size', default=0.3) # By default its 0.5
    mapping_voxel_points = LaunchConfiguration('mapping.max_points_per_voxel', default=10) # By default its 20  #PROVA A FAR VARIARE SOLO QUESTO!!!
    data_deskew = LaunchConfiguration('data.deskew', default=True) # Enable manipulation of max and min range
    base_frame = LaunchConfiguration('base_frame', default='')  # (base_link/base_footprint)
    lidar_odom_frame = LaunchConfiguration('lidar_odom_frame', default='odom_lidar')
    publish_odom_tf = LaunchConfiguration('publish_odom_tf', default=True)
    invert_odom_tf = LaunchConfiguration('invert_odom_tf', default=True)
    max_num_iterations = LaunchConfiguration('registration.max_num_iterations', default=500) # By default its 500
    convergence_criterion = LaunchConfiguration('registration.convergence_criterion', default=0.0001) # By default its 0.0001

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

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': use_sim_time,
            }],
        ),
        Node(
            package='tf2_ros',
            name='static_transform_map_to_base_link',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
        ),
        Node(
            package='tf2_ros',
            name='static_transform_base_link_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
        ),

        ExecuteProcess(
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

        Node(
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios16p_node',
            output='screen',
            parameters=[{'config_path': lidar_config_file}],
            condition=UnlessCondition(play_bag),
        ),

        Node(
            package='kiss_icp',
            executable='kiss_icp_node',
            name='kiss_icp_node',
            output='screen',
            remappings=[
                ('pointcloud_topic', pointcloud_topic),
        ],
            parameters=[


            #default_config_file_path, # Default configuration file

            custom_config_file_path, # Custom configuration file


                {#///kiss-ICP's configuration\\\
                    
                 'publish_debug_clouds': visualize, # Toggle rviz visualization
                 'use_sim_time': use_sim_time,      # Toggle simulation time

                # Main parameters to tune for performance evaluation

                #  'base_frame': base_frame,              
                #  'data.deskew': data_deskew,
                #  'data.max_range': max_range,
                #  'data.min_range': min_range,
                #  'invert_odom_tf': invert_odom_tf,
                #  'lidar_odom_frame': lidar_odom_frame,      
                #  'mapping.max_points_per_voxel': mapping_voxel_points,
                #  'mapping.voxel_size': mapping_voxel_size,
                #  'publish_odom_tf': publish_odom_tf,                
                #  'registration.convergence_criterion': convergence_criterion,
                #  'registration.max_num_iterations': max_num_iterations,
                 
                # More parameters available for tuning in the configuration files

                 #'adaptive_threshold.initial_threshold',
                 #'adaptive_threshold.min_motion_th',
                 #'registration.max_num_threads':,
                 #'orientation_covariance': orientation_covariance, 
                 #'position_covariance': position_covariance,
                },       
            ],
        ),


        Node(
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
