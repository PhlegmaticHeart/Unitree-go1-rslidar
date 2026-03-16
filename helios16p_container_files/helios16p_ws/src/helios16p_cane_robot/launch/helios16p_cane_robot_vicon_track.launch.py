from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
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

    lidar_config_file = os.path.join(pkg_share, 'configs', 'lidar_config.yaml') # RSLidar's config file path

    rviz_config_file = os.path.join(pkg_share, 'configs', 'rviz_vicon.rviz') # Rviz2 config file path

    vicon_package=get_package_share_directory('vicon_receiver')

    vicon_launch_path = os.path.join(vicon_package, 'launch', 'client.launch.py')


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


# ----------------------------------- Kiss-ICP's debug parameters -----------------------------------

    declare_visualize_arg = DeclareLaunchArgument(
        'visualize',
        default_value='False',
        description='Flag to enable rviz visualization'
    )
    visualize = LaunchConfiguration('visualize') # Flag to enable rviz visualization

    declare_base_frame_arg = DeclareLaunchArgument(
        'base_frame',
        default_value='',
        description='Base frame for the robot'
    )
    base_frame = LaunchConfiguration('base_frame')  # (base_link/base_footprint)


    declare_vicon_obj_frame_arg = DeclareLaunchArgument(
        'vicon_frame',
        default_value='go1_go1',
        description='Vicon frame for the robot'
    )
    vicon_obj_frame = LaunchConfiguration('vicon_frame')  # vicon frame for the robot, by default its set to go1_go1 as in the vicon system the robot is named go1 and the object tracked is named go1 as well


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

# ----------------------------------- Nodes -----------------------------------

    publisher_node = Node( # Publish robot state
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': use_sim_time,
            }],
        )


    tf2_map_to_vicon = Node( # Static transform from map to vicon
            package='tf2_ros',
            name='static_transform_map_to_vicon',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'vicon'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    tf2_vicon_to_vicon_obj_frame = Node( # Static transform from vicon to vicon_obj_frame
            package='tf2_ros',
            name='static_transform_vicon_to_vicon_obj_frame',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'vicon', vicon_obj_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    tf2_vicon_obj_frame_to_base_link = Node( # Static transform from vicon_obj_frame to base_link
            package='tf2_ros',
            name='static_transform_vicon_obj_frame_to_base_link',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', vicon_obj_frame, base_frame],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    tf2_base_link_to_rslidar = Node( # Static transform from base_link to rslidar
            package='tf2_ros',
            name='static_transform_base_link_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', base_frame, 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        )


    lidar_driver_node = Node( # Driver node
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios16p_node',
            output='screen',
            parameters=[{'config_path': lidar_config_file}],
            condition=UnlessCondition(simulate)
        )


    vicon_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(vicon_launch_path),
        launch_arguments={
            'hostname': '192.168.50.56',
            'topic_namespace': 'vicon', 
            'buffer_size': '200',
            'world_frame': 'map',
            'vicon_frame': 'vicon',
            'map_xyz': '[0.0, 0.0, 0.0]',
            'map_rpy': '[0.0, 0.0, 0.0]',
            'map_rpy_in_degrees': 'false'
        }.items(),
        condition=UnlessCondition(simulate)

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
        declare_visualize_arg,
        declare_base_frame_arg,
        declare_vicon_obj_frame_arg,
        declare_config_name_arg,

        publisher_node,
        tf2_map_to_vicon,
        tf2_vicon_to_vicon_obj_frame,
        tf2_vicon_obj_frame_to_base_link,
        tf2_base_link_to_rslidar,
        lidar_driver_node,
        vicon_launch,
        rviz2_node,


    ]   
)
