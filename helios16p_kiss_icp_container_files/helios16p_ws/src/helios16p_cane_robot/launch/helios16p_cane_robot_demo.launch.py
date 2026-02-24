from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
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

    lidar_config_file = os.path.join(pkg_share, 'configs', 'lidar_config.yaml') # RSLidar's config file path

    rviz_config_file = os.path.join(pkg_share, 'configs', 'launchrviz.rviz') # Rviz2 config file path

    bag_path = '' # Bag file path

    go1_package=get_package_share_directory('go1_description')

    go1_launch_path = os.path.join(go1_package, 'launch', 'go1_demo.launch.py')

    kiss_package=get_package_share_directory('kiss_icp')
   
    kiss_launch_path = os.path.join(kiss_package, 'launch', 'odometry.launch.py')

# ----------------------------------- Simulation and bag flags parameters -----------------------------------

    declare_simulate_arg = DeclareLaunchArgument(
        'simulate',
        default_value='False',
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
        description='Flag to disable map->odom_lidar transform for better performance evaluation of kiss-ICP'
    )
    nomap = LaunchConfiguration('nomap') # Flag to disable map->odom_lidar

# ----------------------------------- Kiss-ICP's debug parameters -----------------------------------

    declare_visualize_arg = DeclareLaunchArgument(
        'visualize',
        default_value='True',
        description='Flag to enable rviz visualization'
    )
    visualize = LaunchConfiguration('visualize') # Flag to enable rviz visualization


    declare_visualize_clouds_arg = DeclareLaunchArgument(
        'visualize_clouds',
        default_value=visualize,
        description='Flag to enable rviz visualization of clouds published by kiss-ICP'
    )
    visualize_clouds = LaunchConfiguration('visualize_clouds') # Flag to enable rviz visualization of clouds published by kiss-ICP


    declare_nokiss_arg = DeclareLaunchArgument(
        'nokiss',
        default_value='False',
        description='Flag to disable kiss-ICP'
    )
    nokiss = LaunchConfiguration('nokiss') # Flag to enable rviz visualization


    declare_max_range_arg = DeclareLaunchArgument(
        'data.max_range',
        default_value='30.0',
        description='Maximum range for pointcloud data filtering'
    )
    max_range = LaunchConfiguration('data.max_range') # By default its 100


    declare_min_range_arg = DeclareLaunchArgument(
        'data.min_range',
        default_value='0.2',
        description='Minimum range for pointcloud data filtering'
    )    
    min_range = LaunchConfiguration('data.min_range') # By default its 0


    declare_voxel_size_arg = DeclareLaunchArgument(
        'mapping.voxel_size',
        default_value='0.3',
        description='Voxel size for mapping'
    )    
    mapping_voxel_size = LaunchConfiguration('mapping.voxel_size') # By default its 0.5


    declare_max_points_arg = DeclareLaunchArgument(
        'mapping.max_points_per_voxel',
        default_value='10',
        description='Maximum points per voxel for mapping'
    )    
    mapping_voxel_points = LaunchConfiguration('mapping.max_points_per_voxel') # By default its 20


    declare_deskew_arg = DeclareLaunchArgument(
        'data.deskew',
        default_value='True',
        description='Enable deskew for pointcloud data'
    )
    data_deskew = LaunchConfiguration('data.deskew') # Enable manipulation of max and min range


    declare_base_frame_arg = DeclareLaunchArgument(
        'base_frame',
        default_value='base',
        description='Base frame for the robot'
    )
    base_frame = LaunchConfiguration('base_frame')  # (base_link/base_footprint)


    declare_odom_frame_arg = DeclareLaunchArgument(
        'lidar_odom_frame',
        default_value='odom_lidar',
        description='Name of the lidar odometry frame'
    )
    lidar_odom_frame = LaunchConfiguration('lidar_odom_frame') # It gives the name to the frame of the odometry published by kiss-ICP


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


    declare_max_num_iterations_arg = DeclareLaunchArgument(
        'max_num_iterations',
        default_value='700',
        description='Maximum number of iterations for registration'
    )
    max_num_iterations = LaunchConfiguration('registration.max_num_iterations') # By default its 500


    declare_convergence_criterion_arg = DeclareLaunchArgument(
        'convergence_criterion',
        default_value='0.0001',
        description='Convergence criterion for registration'
    )    
    convergence_criterion = LaunchConfiguration('registration.convergence_criterion') # By default its 0.0001


    declare_config_name_arg = DeclareLaunchArgument(
        'setrange',
        default_value='mrange100.yaml',
        description='Name of kiss-icp yaml configuration to load'
    )
    config_name = LaunchConfiguration('setrange') # Configuration file name to load, by default its set to 100m range


    config_name_path = PathJoinSubstitution([
        FindPackageShare(package_name),  
        'configs',
        config_name
    ])
# ----------------------------------- Topics' configuration -----------------------------------

    declare_topic_arg = DeclareLaunchArgument(
        'topic',
        default_value='/rslidar_points',   # Driver's topic
        description='Input pointcloud topic for KISS-ICP'
    )
    pointcloud_topic = LaunchConfiguration('topic')


# ----------------------------------- Nodes -----------------------------------


    go1_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(go1_launch_path),
         launch_arguments={
                'use_jsp': 'none',
                'use_rviz': 'false'
                }.items()
        )

    tf2_map_to_odom_lidar = Node( # Static transform from map to base_frame
            package='tf2_ros',
            name='static_transform_map_to_odom_lidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', lidar_odom_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )
    

    tf2_odom_lidar_to_base_frame = Node( # Static transform from odom_lidar to base_frame
            package='tf2_ros',
            name='static_transform_odom_lidar_to_base_frame',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', lidar_odom_frame, base_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
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
                '--clock', '1.0',
                '--loop'
            ],
            output='screen',
            condition=IfCondition(play_bag),
            name='startmybag'
        )


    lidar_driver_node = Node( # Driver node
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios16p_node',
            output='screen',
            parameters=[{'config_path': lidar_config_file}],
            condition=UnlessCondition(simulate)
        )


    kiss_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(kiss_launch_path),
            launch_arguments={
                'visualize': visualize,
                'config_file': config_name_path,
                'use_sim_time': use_sim_time,
                'topic': pointcloud_topic,
                'base_frame': base_frame,
                'lidar_odom_frame': lidar_odom_frame,
                'publish_odom_tf': publish_odom_tf,
                'invert_odom_tf': invert_odom_tf,
            }.items(),
            condition=UnlessCondition(nokiss)
        )

    rviz2_node = Node( # Rviz2 node
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=[
                '-d',
                rviz_config_file
            ],
            parameters=[{'use_sim_time' : use_sim_time}],
            condition=IfCondition(visualize)
        )


# ----------------------------------- Nodes and commands execution -----------------------------------

    return LaunchDescription([

        declare_simulate_arg,
        declare_use_sim_time_arg,
        declare_play_bag_arg,
        declare_bagfile_arg, 
        declare_nomap_arg,  
        declare_visualize_arg,
        declare_visualize_clouds_arg,
        declare_nokiss_arg,
        declare_max_range_arg,
        declare_min_range_arg,
        declare_voxel_size_arg,
        declare_max_points_arg,
        declare_deskew_arg,
        declare_base_frame_arg,
        declare_odom_frame_arg,
        declare_publish_odom_tf_arg,
        declare_invert_odom_tf_arg,
        declare_max_num_iterations_arg,
        declare_convergence_criterion_arg,
        declare_topic_arg,
        declare_config_name_arg,

        go1_launch,
        tf2_map_to_odom_lidar,
        tf2_odom_lidar_to_base_frame,
        tf2_base_frame_to_rslidar,
        bag_start_process,
        lidar_driver_node,
        kiss_launch,
        rviz2_node,

    ]   
)
