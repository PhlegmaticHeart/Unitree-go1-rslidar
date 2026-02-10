
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
     return LaunchDescription([

          DeclareLaunchArgument(name='fixed_frame', default_value='base',
                                description='Fixed frame for RVIZ'),
          DeclareLaunchArgument(name='namespace', default_value='',
                                description=
                                   'Choose a namespace for the launched topics.'),
          SetLaunchConfiguration(name='model',
                                 value=PathJoinSubstitution([FindPackageShare('go1_description'),
                                                             'xacro',
                                                             'robot.xacro'])),
     
          Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               parameters=[{
                    'robot_description':
                         ParameterValue(
                              Command([
                                   'xacro ',
                                   LaunchConfiguration('model'),
                              ]),
                              value_type=str
                         ),
                    'frame_prefix': [LaunchConfiguration('namespace'), '/']
               }],
               namespace=LaunchConfiguration('namespace')
          ),


    ])