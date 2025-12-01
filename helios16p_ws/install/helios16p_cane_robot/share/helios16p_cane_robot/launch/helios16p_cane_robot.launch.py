from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, FileContent, PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition 
import os


# configurazione di kiss_icp
default_config_file = os.path.join(
    get_package_share_directory('kiss_icp'), 'config', 'config.yaml'
)


#flags di simulazione
def generate_launch_description():
    simulation = LaunchConfiguration('simulation', default='false') #flag simulazione tempo simulato + bag
    use_sim_time = LaunchConfiguration('use_sim_time', default=simulation) #flag tempo simulato
    play_bag = LaunchConfiguration('play_bag', default=simulation)  # flag per rosbag e path della bag
    bagfile = LaunchConfiguration('bagfile', default='/home/ph/bagrecords/rosbag2_2025_11_17-16_12_04/')
    
#configurazione dei topic
    declare_topic_arg = DeclareLaunchArgument( 
        "topic",
        default_value="/rslidar_points",   #topic del driver
        description="Input pointcloud topic for KISS-ICP"
    )
    pointcloud_topic = LaunchConfiguration('topic') 
    visualize = LaunchConfiguration('visualize', default='true')

    base_frame = LaunchConfiguration("base_frame", default="")  # (base_link/base_footprint)
    lidar_odom_frame = LaunchConfiguration("lidar_odom_frame", default="odom_lidar")
    publish_odom_tf = LaunchConfiguration("publish_odom_tf", default=True)
    invert_odom_tf = LaunchConfiguration("invert_odom_tf", default=True)

    position_covariance = LaunchConfiguration("position_covariance", default=0.1)
    orientation_covariance = LaunchConfiguration("orientation_covariance", default=0.1)

    config_file = LaunchConfiguration("config_file", default=default_config_file)
#    urdf_path = PathJoinSubstitution([
#        FindPackageShare('helios16p_cane_robot'), 'urdf', 'helios16p.urdf'
#    ])
    return LaunchDescription([
        declare_topic_arg,

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',                                   #path dell'urdf del robot
            parameters=[{'robot_description': FileContent('/home/ph/ws/helios16p_ws/src/helios16p_cane_robot/urdf/helios16p.urdf'), 'use_sim_time' : use_sim_time }]
        ),
        Node(
            package='tf2_ros',
            name='static_transform_map_to_base_link',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link'],
            output='screen'
        ),
        Node(
            package='tf2_ros',
            name='static_transform_base_link_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rslidar'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play',
                '--rate', '1',
                bagfile,
                '--clock', '1.0', '--loop'
            ],
            output='screen',
            condition=IfCondition(play_bag),
            name='startmybag',
        ),

         Node(
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='helios_16p_node',
            output='screen',
            condition=UnlessCondition(play_bag),
        ),

        Node(
            package='kiss_icp',
            executable="kiss_icp_node",
            name="kiss_icp_node",
            output="screen",
            remappings=[
                ("pointcloud_topic", pointcloud_topic),
        ],
            parameters=[
            {
                #configurazione di kiss_icp
                "base_frame": base_frame,
                "lidar_odom_frame": lidar_odom_frame,
                "publish_odom_tf": publish_odom_tf,
                "invert_odom_tf": invert_odom_tf,
                #configurazione della CLI di kiss_icp
                "publish_debug_clouds": visualize,
                "use_sim_time": use_sim_time,
                "position_covariance": position_covariance,
                "orientation_covariance": orientation_covariance,
            },
            config_file,
        ],
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            output="screen",
            arguments=[
                "-d",
                PathJoinSubstitution([FindPackageShare("kiss_icp"), "rviz", "kiss_icp.rviz"]),
            ],
            parameters=[{'use_sim_time' : use_sim_time}],
            condition=IfCondition(visualize),
    )

        


    
    ])