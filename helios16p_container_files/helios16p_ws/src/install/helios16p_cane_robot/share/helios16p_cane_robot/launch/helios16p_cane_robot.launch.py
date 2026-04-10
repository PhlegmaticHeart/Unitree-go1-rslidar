from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterFile
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro
import os

package_name = 'helios16p_cane_robot'



def generate_launch_description():


# ----------------------------------- Files' path retrieval -----------------------------------

    pkg_share = FindPackageShare('helios16p_cane_robot').find('helios16p_cane_robot') # Package share directory

    xacro_file = os.path.join(pkg_share, 'urdf', 'helios16p.urdf.xacro') # Robot's xacro file path

    robot_description = xacro.process_file(xacro_file).toxml() # Robot description in xml format, keep in mind that this model requires xacro package

    rviz_config_file = os.path.join(pkg_share, 'configs', 'launchrviz.rviz') # Rviz2 config file path

    lidar_config_file = os.path.join(pkg_share, 'configs', 'lidar_config_mr8.yaml') # RSLidar's config file path

    bag_path = '' # Bag file path

    pointcloud_to_laserscan_package=get_package_share_directory('pointcloud_to_laserscan') # pointcloud_to_laserscan package share directory, necessary for the configuration of the pointcloud_to_laserscan node in the rviz config file

    pointcloud_to_laserscan_launch_path = os.path.join(pointcloud_to_laserscan_package, 'launch', 'helios16p_pointcloud_to_laserscan_launch.py')

    unitree_legged_real_package=get_package_share_directory('unitree_legged_real') # unitree_legged_real package share directory, necessary for the configuration of the unitree_legged_real node in the rviz config file

    unitree_legged_real_launch_path = os.path.join(unitree_legged_real_package, 'launch', 'helios16p_high_no_desc.launch.py')

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

    declare_statepublisher_arg = DeclareLaunchArgument(
        'state_publisher',
        default_value='False',
        description='Flag to enable robot state publisher'
    )
    statepublisher = LaunchConfiguration('state_publisher') # Flag to enable robot state publisher

    declare_lidar_config_arg = DeclareLaunchArgument(
        'lidar_config',
        default_value=lidar_config_file,
        description='Path to the lidar configuration file'
    )
    lidar_config = LaunchConfiguration('lidar_config') # Lidar configuration file path

    declare_nomap_arg = DeclareLaunchArgument(
        'nomap',
        default_value='True',
        description='Flag to disable map->odom transform for better performance evaluation of kiss-ICP'
    )
    nomap = LaunchConfiguration('nomap') # Flag to disable map->odom

    declare_compressed_clouds_arg = DeclareLaunchArgument(
        'compressed_clouds',
        default_value='True',
        description='Flag to enable compressed pointclouds'
    )
    compressed_clouds = LaunchConfiguration('compressed_clouds') # Flag to enable compressed pointclouds




# ----------------------------------- Unitree legged real's debug parameters -----------------------------------

    declare_enable_internal_publish_arg = DeclareLaunchArgument(
            'enable_internal_publish',
            default_value='False',
            description='Whether to enable internal publish of go1 internal odometry and imu (True/False)'
        )

    enable_internal_publish_arg = LaunchConfiguration('enable_internal_publish')


    declare_internal_odom_go1_frame_name_arg = DeclareLaunchArgument(
            'internal_odom_frame',
            default_value='internal_odom_go1',
            description='The name of the go1 internal calculated odometry frame to broadcast'
        )
    internal_odom_go1_frame_name_arg = LaunchConfiguration('internal_odom_frame')

    declare_internal_imu_go1_frame_name_arg = DeclareLaunchArgument(
            'internal_imu_frame',
            default_value='internal_imu_go1',
            description='The name of the base frame linked to internal go1 odometry to broadcast'
        )
    internal_imu_go1_frame_name_arg = LaunchConfiguration('internal_imu_frame')

    declare_internal_odom_go1_topic_name_arg = DeclareLaunchArgument(
            'internal_odom_topic',
            default_value='internal_odom_go1',
            description='The name of the internal calculated odometry topic to publish'
        )
    internal_odom_go1_topic_name_arg = LaunchConfiguration('internal_odom_topic')

    declare_internal_imu_go1_topic_name_arg = DeclareLaunchArgument(
            'internal_imu_topic',
            default_value='internal_imu_go1',
            description='The name of the internal imu topic to publish'
        )
    internal_imu_go1_topic_name_arg = LaunchConfiguration('internal_imu_topic')
    
    declare_internal_base_go1_topic_name_arg = DeclareLaunchArgument(
            'internal_base_topic',
            default_value='internal_link_go1',
            description='The name of the internal base topic to publish'
        )
    internal_base_go1_topic_name_arg = LaunchConfiguration('internal_base_topic')



# ----------------------------------- Kiss-ICP's debug parameters -----------------------------------

    declare_visualize_arg = DeclareLaunchArgument(
        'visualize',
        default_value='False',
        description='Flag to enable rviz visualization'
    )
    visualize = LaunchConfiguration('visualize') # Flag to enable rviz visualization

    declare_nolidar_arg = DeclareLaunchArgument(
        'nolidar',
        default_value='False',
        description='Flag to disable lidar driver'
    )
    nolidar = LaunchConfiguration('nolidar') # Flag to disable lidar driver

    declare_visualize_clouds_arg = DeclareLaunchArgument(
        'visualize_clouds',
        default_value='True',
        description='Flag to enable rviz visualization of clouds published by kiss-ICP'
    )
    visualize_clouds = LaunchConfiguration('visualize_clouds') # Flag to enable rviz visualization of clouds published by kiss-ICP

    declare_nolegged_arg = DeclareLaunchArgument(
        'nolegged',
        default_value='False',
        description='Flag to disable legged robot'
    )
    nolegged = LaunchConfiguration('nolegged') # Flag to disable legged robot

    declare_noscan_arg = DeclareLaunchArgument(
        'noscan',
        default_value='False',
        description='Flag to disable scan'
    )
    noscan = LaunchConfiguration('noscan') # Flag to disable scan

    declare_nokiss_arg = DeclareLaunchArgument(
        'nokiss',
        default_value='False',
        description='Flag to disable kiss-ICP'
    )
    nokiss = LaunchConfiguration('nokiss') # Flag to enable rviz visualization


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


    declare_kiss_config_name_arg = DeclareLaunchArgument(
        'setrange',
        default_value='mrange100.yaml',
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

    publisher_node = Node( # Publish robot state
            package='robot_state_publisher',
            name='robot_state_publisher_node',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': use_sim_time,
                'publish_frequency': 20.0 # For minor impact on resources as the default is 50Hz
            }],
            condition=IfCondition(statepublisher)
        )

    tf2_map_to_odom = Node( # Static transform from map to odom
            package='tf2_ros',
            name='static_transform_map_to_odom',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', odom_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen',
            condition=UnlessCondition(nomap),
        )


    tf2_base_frame_to_rslidar = Node( # Static transform from base_link to rslidar
            package='tf2_ros',
            name='static_transform_base_frame_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', base_frame, 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    unitree_legged_real_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(unitree_legged_real_launch_path),
        launch_arguments={
            'enable_internal_publish': enable_internal_publish_arg, # Disable frame broadcasting in the unitree_legged_real node as we are already publishing the necessary frames with static_transform_publisher nodes in this launch file
            'internal_odom_frame': internal_odom_go1_frame_name_arg, # Set the odom frame name in the unitree_legged_real node to be the same as the one published by kiss-ICP for better integration in rviz and easier performance evaluation
            'internal_imu_frame': internal_imu_go1_frame_name_arg, # Set the base frame name in the unitree_leg
            'internal_odom_topic': internal_odom_go1_topic_name_arg, # Set the odom topic name in the unitree_legged_real node to be different from the one published by kiss-ICP to avoid confusion in rviz and for better performance evaluation
            'internal_imu_topic': internal_imu_go1_topic_name_arg, # Set the imu topic name in
            'internal_base_topic': internal_base_go1_topic_name_arg # Set the base topic name in the unitree_legged_real node to be different from the one published by kiss-ICP to avoid confusion in rviz and for better performance evaluation
            }.items(),
        condition=UnlessCondition(nolegged)
        )


    lidar_driver_node = Node( # Driver node
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios16p_node',
            output='screen',
            parameters=[{'config_path': lidar_config}],
            condition=UnlessCondition(nolidar)
        )


    cloudini_node = Node(
            package='cloudini_ros',
            name='cloudini_rslidar_pointcloud_converter',
            executable='cloudini_topic_converter',
            parameters=[{
                'compressing': True,
                'topic_input': pointcloud_topic,
                'topic_output': PathJoinSubstitution([pointcloud_topic, 'compressed']),
                'resolution': 0.001,
            }],
            condition=IfCondition(compressed_clouds)
        )



    pointcloud_to_laserscan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(pointcloud_to_laserscan_launch_path),
         #launch_arguments={
         #      }.items()
        condition=UnlessCondition(noscan)
        )


    bag_start_process = ExecuteProcess( # Bag file playback
            cmd=[
                'ros2', 'bag', 'play',
                '--rate', '1.0',
                bagfile,
                '--clock', '1.0',# '--loop',
                '--topics', '/rslidar_points',
            ],
            output='screen',
            condition=IfCondition(play_bag),
            name='start_my_bag'
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
        declare_visualize_arg,
        declare_nolidar_arg,
        declare_visualize_clouds_arg,
        declare_compressed_clouds_arg,
        declare_statepublisher_arg,
        declare_lidar_config_arg,
        declare_enable_internal_publish_arg,
        declare_internal_odom_go1_frame_name_arg,
        declare_internal_imu_go1_frame_name_arg,
        declare_internal_odom_go1_topic_name_arg,
        declare_internal_imu_go1_topic_name_arg,
        declare_internal_base_go1_topic_name_arg,


        declare_nolegged_arg,
        declare_noscan_arg,
        declare_nokiss_arg,
        declare_nomap_arg,
        declare_base_frame_arg,
        declare_odom_frame_arg,
        declare_publish_odom_tf_arg,
        declare_invert_odom_tf_arg,
        declare_topic_arg,
        declare_kiss_config_name_arg,

        publisher_node,
        tf2_map_to_odom,
        tf2_base_frame_to_rslidar,
        lidar_driver_node,
        kiss_node,
        unitree_legged_real_launch,
        pointcloud_to_laserscan_launch,
        cloudini_node,
        bag_start_process,
        rviz2_node,

    ]
)
