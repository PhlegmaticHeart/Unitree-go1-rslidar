#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rosgraph_msgs.msg import Clock

class SimulationTimeLidar(Node):
    def __init__(self):
        super().__init__('simulation_time_lidar')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.callback,
            10
        )
        self.publisher = self.create_publisher(LaserScan, '/scan_simulation_time', 10)
        
        # Subscribe to the /clock topic and store the simulation time
        self.simulation_time = None
        self.clock_subscription = self.create_subscription(
            Clock,
            '/clock',
            self.clock_callback,
            10
        )
    def callback(self, scan):
        # Retrieve the simulation time
        simulation_time = self.get_simulation_time()
        # Update the header timestamp of the LaserScan message
        scan.header.stamp = simulation_time
        # Republish the modified LaserScan message
        self.publisher.publish(scan)
    def clock_callback(self, clock_msg):
        self.simulation_time = clock_msg.clock
    def get_simulation_time(self):
        if self.simulation_time is None:
            return self.get_clock().now()
        return self.simulation_time
        
def main(args=None):
    rclpy.init(args=args)
    node = SimulationTimeLidar()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
