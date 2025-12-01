from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    package_arg = DeclareLaunchArgument(
        'urdf_package',
        description='The package where the robot description is located',
        default_value='urdf_sim_tutorial'
    )

    model_arg = DeclareLaunchArgument(
        'urdf_package_path',
        description='The path to the robot description relative to the package root',
        default_value='urdf/10-firsttransmission.urdf.xacro'
    )

    rvizconfig_arg = DeclareLaunchArgument(
        'rvizconfig',
        default_value=PathJoinSubstitution(
            [FindPackageShare('urdf_tutorial'), 'rviz', 'urdf.rviz']
        ),
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare('urdf_sim_tutorial'), 'launch', 'gazebo.launch.py']
            )
        ),
        launch_arguments={
            'urdf_package': LaunchConfiguration('urdf_package'),
            'urdf_package_path': LaunchConfiguration('urdf_package_path')
        }.items(),
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    load_joint_state_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'joint_state_broadcaster'],
        output='screen'
    )

    load_head_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'head_controller'],
        output='screen'
    )

    return LaunchDescription([
        package_arg,
        model_arg,
        rvizconfig_arg,
        gazebo_launch,
        rviz_node,
        load_joint_state_controller,
        load_head_controller,
    ])
