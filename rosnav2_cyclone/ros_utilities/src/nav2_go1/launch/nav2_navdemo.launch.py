from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

package_name = 'nav2_go1'



def generate_launch_description():


# ----------------------------------- Files' path retrieval -----------------------------------

    nav2_bringup_package=get_package_share_directory('nav2_bringup') # pointcloud_to_laserscan package share directory, necessary for the configuration of the pointcloud_to_laserscan node in the rviz config file

    nav2_bringup_launch_path = os.path.join(nav2_bringup_package, 'launch', 'bringup_launch.py')

    nav2_wrapper_dir=get_package_share_directory(package_name) # pointcloud_to_laserscan package share directory, necessary for the configuration of the pointcloud_to_laserscan node in the rviz config file

    nav2_custom_bringup_launch_path = os.path.join(nav2_wrapper_dir, 'launch', 'custom_bringup.launch.py')


# ----------------------------------- Simulation and bag flags parameters -----------------------------------


#    declare_config_name_arg = DeclareLaunchArgument(
#        'setrange',
#        default_value='mrange100.yaml',
#        description='Name of kiss-icp yaml configuration to load'
#    )
#    config_name = LaunchConfiguration('setrange') # Configuration file name to load, by default its set to 100m range



# ----------------------------------- Nodes -----------------------------------


    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_custom_bringup_launch_path),
         launch_arguments={
            'use_sim_time': 'false',
            'autostart': 'true',
            'map': '/home/admin/maps/ufficio/map.yaml',
            'params_file': '/home/admin/nav2_params.yaml'
        }.items()
    )


    rviz2_node = Node( # Rviz2 node
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=[
                '-d',
                '/opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz'
            ]
            #condition=IfCondition(visualize)
        )


# ----------------------------------- Nodes and commands execution -----------------------------------

    return LaunchDescription([

        nav2_bringup_launch,
        rviz2_node

    ]
)
