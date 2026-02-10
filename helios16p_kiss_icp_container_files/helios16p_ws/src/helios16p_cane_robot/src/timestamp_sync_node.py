import rclpy
from sensor_msgs.msg import PointCloud2
   
rclpy.init()
node = rclpy.create_node('sync_node')
pub = node.create_publisher(PointCloud2, '/rslidar_points_fixed', 10)
sub = node.create_subscription(PointCloud2, '/rslidar_points', lambda msg: (setattr(msg.header, 'stamp', node.get_clock().now().to_msg()), pub.publish(msg)), 10)
rclpy.spin(node)
rclpy.shutdown()
