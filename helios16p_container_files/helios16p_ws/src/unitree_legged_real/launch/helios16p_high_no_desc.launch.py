
"""
Launches high level go controls for the go1
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():

    declare_enable_internal_publisher_arg = DeclareLaunchArgument(
        'enable_internal_publish',
        default_value='False',
        description='Whether to enable internal publish (True/False)'
    )

    enable_internal_publish = LaunchConfiguration('enable_internal_publish')

    declare_frame_arg_odom_frame_arg = DeclareLaunchArgument(
        'internal_odom_frame',
        default_value='internal_odom_go1',
        description='The name of the odom frame to broadcast'
    )

    odom_frame = LaunchConfiguration('internal_odom_frame')

    declare_frame_arg_imu_frame_arg = DeclareLaunchArgument(
        'internal_imu_frame',
        default_value='internal_imu_go1',
        description='The name of the imu frame to broadcast'
    )

    imu_frame = LaunchConfiguration('internal_imu_frame')
    declare_frame_arg_odom_topic_arg = DeclareLaunchArgument(
        'internal_odom_topic',
        default_value='internal_odom_go1',
        description='The name of the odom topic to publish'
    )

    odom_topic = LaunchConfiguration('internal_odom_topic')

    declare_frame_arg_imu_topic_arg = DeclareLaunchArgument(
        'internal_imu_topic',
        default_value='internal_imu_go1',
        description='The name of the imu topic to publish'
    )

    imu_topic = LaunchConfiguration('internal_imu_topic')

    declare_frame_arg_link_topic_arg = DeclareLaunchArgument(
        'internal_base_topic',
        default_value='internal_link_go1',
        description='The name of the base topic to publish'
    )

    link_topic = LaunchConfiguration('internal_base_topic')


    udp_high_node = Node(
        package='unitree_legged_real',
        executable='udp_high',
        output='screen',
        parameters=[
            {"enable_internal_publish": enable_internal_publish},  # Set to True to enable internal publish
            {"internal_odom_frame": odom_frame},  # Set the odom frame name
            {"internal_imu_frame": imu_frame},  # Set the imu frame name
            {"internal_odom_topic": odom_topic},  # Set the odom topic name
            {"internal_imu_topic": imu_topic},  # Set the imu topic name
            {"internal_base_topic": link_topic}  # Set the base topic name
        ],
        name='udp_high_node'
        )

    jsp_high_node = Node(
        package='unitree_legged_real',
        executable='jsp_high',
        output='screen',
        name='jsp_high_node'
        )
    
    cmd_processor_node = Node(
        package='unitree_nav',
        executable='cmd_processor',
        output='screen',
        name='cmd_processor_node'

        )
    
    return LaunchDescription([
            declare_enable_internal_publisher_arg,
            declare_frame_arg_odom_frame_arg,
            declare_frame_arg_imu_frame_arg,
            declare_frame_arg_odom_topic_arg,
            declare_frame_arg_imu_topic_arg,
            declare_frame_arg_link_topic_arg,

            udp_high_node,
            jsp_high_node,
            cmd_processor_node
    ]
    )