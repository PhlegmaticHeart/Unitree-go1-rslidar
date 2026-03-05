
"""
Launches high level go controls for the go1
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():

    declare_enable_frame_arg = DeclareLaunchArgument(
        'enable_frame',
        default_value='False',
        description='Whether to enable frame broadcasting (True/False)'
    )

    enable_frame = LaunchConfiguration('enable_frame')

    declare_frame_arg_odom_frame_arg = DeclareLaunchArgument(
        'odom_frame',
        default_value='odom_go1',
        description='The name of the odom frame to broadcast'
    )

    odom_frame = LaunchConfiguration('odom_frame')

    declare_frame_arg_imu_frame_arg = DeclareLaunchArgument(
        'imu_frame',
        default_value='imu_go1',
        description='The name of the base frame to broadcast'
    )

    imu_frame = LaunchConfiguration('imu_frame')
    declare_frame_arg_odom_topic_arg = DeclareLaunchArgument(
        'odom_topic',
        default_value='odom_go1',
        description='The name of the odom topic to publish'
    )

    odom_topic = LaunchConfiguration('odom_topic')

    declare_frame_arg_imu_topic_arg = DeclareLaunchArgument(
        'imu_topic',
        default_value='imu_go1',
        description='The name of the imu topic to publish'
    )

    imu_topic = LaunchConfiguration('imu_topic')




    udp_high_node = Node(
        package='unitree_legged_real',
        executable='udp_high',
        output='screen',
        parameters=[
            {"enable_frame": enable_frame},  # Set to True to enable frame broadcasting
            {"odom_frame": odom_frame},  # Set the odom frame name
            {"imu_frame": imu_frame},  # Set the imu frame name
            {"odom_topic": odom_topic},  # Set the odom topic name
            {"imu_topic": imu_topic}  # Set the imu topic name
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
            declare_enable_frame_arg,
            declare_frame_arg_odom_frame_arg,
            declare_frame_arg_imu_frame_arg,
            declare_frame_arg_odom_topic_arg,
            declare_frame_arg_imu_topic_arg,

            udp_high_node,
            jsp_high_node,
            cmd_processor_node
    ]
    )