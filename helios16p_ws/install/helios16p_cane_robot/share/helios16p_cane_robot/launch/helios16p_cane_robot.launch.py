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
    lidarmaxdistance = LaunchConfiguration('max_distance', default=30.0) #distanza oltre cui i dati sono scarti
    simulation = LaunchConfiguration('simulation', default='false') #flag simulazione tempo simulato + bag
    use_sim_time = LaunchConfiguration('use_sim_time', default=simulation) #flag tempo simulato
    kissmaxrange = LaunchConfiguration('data.max_range', default=30.0) #di base è 100
    kissminrange = LaunchConfiguration('data.min_range', default=0.0) #di base è a 0
    kissmappingvoxelsize = LaunchConfiguration('mapping.voxel_size', default=0.3) #di base è 0.5
    kissmappingvoxelpoints = LaunchConfiguration('mapping.max_points_per_voxel', default=10) #di base è 20
    datadeskew = LaunchConfiguration('data.deskew', default='true') #abilita la manipolazione delle soglie max e min data range
    play_bag = LaunchConfiguration('play_bag', default=simulation)  # flag per rosbag e path della bag
    bagfile = LaunchConfiguration('bagfile', default='/home/ph/bagrecords/bagtest600/rosbag2_600_BIG/') #posizione del file bag da riprodurre
    
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
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        ),
        Node(
            package='tf2_ros',
            name='static_transform_base_link_to_rslidar',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rslidar'],
            parameters=[{'use_sim_time' : use_sim_time}],
            output='screen'
        ),
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play',
                '--rate', '0.2',
                bagfile,
                '--clock', '0.2', '--loop',
                '--topic', '/rslidar_points',
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
            parameters=[{"max_distance": lidarmaxdistance}],
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
                config_file, #file base, i parametri qui sotto hanno valenza prioritaria

                {#///configurazione di kiss_icp\\\
                    
                 #"adaptive_threshold.initial_threshold",
                 #"adaptive_threshold.min_motion_th",
                 "base_frame": base_frame,              
                 "data.deskew": datadeskew,
                 "data.max_range": kissmaxrange,
                 "data.min_range": kissminrange,
                 "invert_odom_tf": invert_odom_tf,
                 "lidar_odom_frame": lidar_odom_frame,      
                 "mapping.max_points_per_voxel": kissmappingvoxelpoints,
                 "mapping.voxel_size": kissmappingvoxelsize,
                 "orientation_covariance": orientation_covariance, 
                 "position_covariance": position_covariance,
                 "publish_debug_clouds": visualize,
                 "publish_odom_tf": publish_odom_tf,                
                 # "registration.convergence_criterion":,
                 # "registration.max_num_iterations":,
                 # "registration.max_num_threads":,
                 "use_sim_time": use_sim_time,

                },
                
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