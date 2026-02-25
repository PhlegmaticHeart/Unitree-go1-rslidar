# ROS 2 pointcloud <-> laserscan converters

This is a ROS 2 package forked from [ros_perception/pointcloud_to_laserscan](https://github.com/ros-perception/pointcloud_to_laserscan/tree/humble), essentially a port of the original ROS 1 package.

The package provides components to convert `sensor_msgs/msg/PointCloud2` messages to `sensor_msgs/msg/LaserScan` messages.

## pointcloud\_to\_laserscan::PointCloudToLaserScanNode

This ROS 2 component projects `sensor_msgs/msg/PointCloud2` messages into `sensor_msgs/msg/LaserScan` messages.

### Published Topics

* `/scan` (`sensor_msgs/msg/LaserScan`) - The output laser scan.

### Subscribed Topics

* `/livox/lidar` (`sensor_msgs/msg/PointCloud2`) - The input point cloud from the Livox-ros-driver2. No input will be processed if there isn't at least one subscriber to the `/scan` topic.

### Parameters

* `min_height` (double, default: 2.2e-308) - The minimum height to sample in the point cloud in meters. 
* `max_height` (double, default: 1.8e+308) - The maximum height to sample in the point cloud in meters.
* `angle_min` (double, default: -π) - The minimum scan angle in radians.
* `angle_max` (double, default: π) - The maximum scan angle in radians.
* `angle_increment` (double, default: π/180) - Resolution of laser scan in radians per ray.
* `queue_size` (double, default: detected number of cores) - Input point cloud queue size.
* `scan_time` (double, default: 1.0/30.0) - The scan rate in seconds. Only used to populate the scan_time field of the output laser scan message.
* `range_min` (double, default: 0.0) - The minimum ranges to return in meters.
* `range_max` (double, default: 1.8e+308) - The maximum ranges to return in meters.
* `target_frame` (str, default: none) - If provided, transform the pointcloud into this frame before converting to a laser scan. Otherwise, laser scan will be generated in the same frame as the input point cloud. 
* `transform_tolerance` (double, default: 0.01) - Time tolerance for transform lookups. Only used if a `target_frame` is provided.
* `use_inf` (boolean, default: true) - If disabled, report infinite range (no obstacle) as range_max + 1. Otherwise report infinite range as +inf.

These parameters can be set based on the [MID360 lidar specs](https://www.livoxtech.com/mid-360/specs).

### Message Timestamp

Since the lidar is used with the real robot (and not in simulation), the timestamp of the `sensor_msgs/msg/LaserScan` message is set to real time.

In case the lidar is also needed in simulation, the header of the message could be changed to follow Gazebo simulation time.
This can be achieved by uncommenting the following lines in "pointcloud_to_laserscan_node.cpp" (lines 148,149):

```
scan_msg->header.stamp = rclcpp::Node::now();
scan_msg->header.frame_id = "livox_frame";
```
