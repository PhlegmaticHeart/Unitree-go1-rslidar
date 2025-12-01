from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios_16p_node',
            output='screen',
            parameters=[
                {'param_file': ''}, #path a file yaml
            ]
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='state_publisher',
            output='screen',
            parameters=[
                {'robot_description': Command(['xacro ', ''])} #path a file xacro
            ]
        )
    ])

