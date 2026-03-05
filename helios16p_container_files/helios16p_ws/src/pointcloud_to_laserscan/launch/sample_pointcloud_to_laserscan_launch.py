from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/livox/lidar'),
                        ('scan', '/scan')],
            parameters=[{
                # keep the same frame as the input point cloud
                'target_frame': "",
                # since target_frame is empty, transform tolerance is not used
                'transform_tolerance': 0.01,
                # parameters to set based on sensor mounting
                'min_height': 0.0,
                'max_height': 1.0,
                # to cover 360 degree field of view
                'angle_min': -3.1415,  # -M_PI
                'angle_max': 3.1415,  # M_PI
                'angle_increment': 0.008, 
                'scan_time': 0.3333,
                # ranges set based on sensor specs
                'range_min': 0.1,
                'range_max': 40.0,
                'use_inf': True,
                'inf_epsilon': 1.0,
                "use_sim_time": True,
            }],
            name='pointcloud_to_laserscan'
        )
    ])
