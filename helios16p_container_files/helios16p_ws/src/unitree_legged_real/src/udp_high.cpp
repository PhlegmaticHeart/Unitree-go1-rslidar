#include "rclcpp/rclcpp.hpp"
#include "ros2_unitree_legged_msgs/msg/high_cmd.hpp"
#include "ros2_unitree_legged_msgs/msg/high_state.hpp"
#include "ros2_unitree_legged_msgs/msg/low_cmd.hpp"
#include "ros2_unitree_legged_msgs/msg/low_state.hpp"
#include "unitree_legged_sdk/unitree_legged_sdk.h"
#include "convert.h"
#include "sensor_msgs/msg/imu.hpp"
#include "nav_msgs/msg/odometry.hpp"
#include "tf2/LinearMath/Quaternion.h"
#include "tf2_geometry_msgs/tf2_geometry_msgs.hpp"

using UNITREE_LEGGED_SDK::UDP;
using UNITREE_LEGGED_SDK::HighCmd;
using UNITREE_LEGGED_SDK::HighState;

class UDPHighBridge
{
public:
  UDP udp;

  HighCmd cmd = {0};
  HighState state = {0};

public:
  UDPHighBridge()
  : udp(8090, "192.168.123.161", 8082, sizeof(HighCmd), sizeof(HighState))
  {
    udp.InitCmdData(cmd);
  }
};

class UDPHighNode : public rclcpp::Node
{
public:
  UDPHighNode()
  : Node("udp_high")
  {
    // Parameters
    auto param = rcl_interfaces::msg::ParameterDescriptor{};
    param.description = "The rate at which the node requests state information over UDP (Hz).";
    declare_parameter("rate", 500.0, param);
    rate_ = get_parameter("rate").get_parameter_value().get<double>();
    interval_ = 1.0 / rate_;

    // Publication Flag
    declare_parameter<bool>("enable_internal_publish", false); // ROS 2 param declaration
    std::atomic<bool> publish_enabled; // corresponding local variable
    publish_enabled = get_parameter("enable_internal_publish").as_bool(); // if true, publish odom and imu with frame_id and broadcast tf; if false, does not publish imu and odom topics does not broadcast tf

    if (publish_enabled) { // if false, does not declare topics and tfs
    // Frame names parametrized, allow names remapping through ROS 2 parameters
    declare_parameter<std::string>("internal_odom_frame", "internal_odom_go1");
    declare_parameter<std::string>("internal_imu_frame", "internal_imu_go1");
    declare_parameter<std::string>("internal_base_frame", "internal_link_go1");
    odom_frame_ = get_parameter("internal_odom_frame").as_string();
    imu_frame_ = get_parameter("internal_imu_frame").as_string();
    link_frame_ = get_parameter("internal_base_frame").as_string();

    // Publishers
    declare_parameter<std::string>("internal_odom_topic", "internal_odom_go1");
    declare_parameter<std::string>("internal_imu_topic", "internal_imu_go1");
    odom_topic_ = get_parameter("internal_odom_topic").as_string();
    imu_topic_ = get_parameter("internal_imu_topic").as_string();

    pub_imu_ = create_publisher<sensor_msgs::msg::Imu>(imu_topic_, 10);
    pub_odom_ = create_publisher<nav_msgs::msg::Odometry>(odom_topic_, 10);
    };
    pub_state_ = create_publisher<ros2_unitree_legged_msgs::msg::HighState>("high_state", 10);
    // Subscriber for commands
    sub_cmd_ = create_subscription<ros2_unitree_legged_msgs::msg::HighCmd>(
      "high_cmd", 10,
      std::bind(&UDPHighNode::cmd_callback, this, std::placeholders::_1)
    );

    RCLCPP_INFO(get_logger(), "udp_high node started");

    if (publish_enabled.load()) {
      RCLCPP_INFO(get_logger(), "Publishing enabled: odom_frame='%s', imu_frame='%s', base_frame='%s'", odom_frame_.c_str(), imu_frame_.c_str(), link_frame_.c_str());
    } else {
      RCLCPP_INFO(get_logger(), "Publishing disabled");
    }

    if (publish_enabled.load()) {
      timer_ = create_wall_timer(
        std::chrono::microseconds(static_cast<int>(interval_ * 1e6)),
        std::bind(&UDPHighNode::timer_callback<true>, this)
      );
    } else {
      timer_ = create_wall_timer(
        std::chrono::microseconds(static_cast<int>(interval_ * 1e6)),
        std::bind(&UDPHighNode::timer_callback<false>, this)
      );
    }

  }

private:

  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<ros2_unitree_legged_msgs::msg::HighState>::SharedPtr pub_state_;
  rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr pub_imu_;
  rclcpp::Publisher<nav_msgs::msg::Odometry>::SharedPtr pub_odom_;
  rclcpp::Subscription<ros2_unitree_legged_msgs::msg::HighCmd>::SharedPtr sub_cmd_;
  double rate_, interval_;

  std::atomic<bool> publish_enabled;   // publish flag
  std::string odom_frame_, imu_frame_, link_frame_;  // frame parameters
  std::string odom_topic_, imu_topic_;  // topic parameters
  UDPHighBridge bridge_;
  ros2_unitree_legged_msgs::msg::HighState state_ros_;

  void cmd_callback(const ros2_unitree_legged_msgs::msg::HighCmd::SharedPtr msg)
  {
    bridge_.cmd = rosMsg2Cmd(msg);
    bridge_.udp.SetSend(bridge_.cmd);
    bridge_.udp.Send();
  }

  template<bool publish_enabled> // if publish is false, then the time_callback is lightened by not initializing odom and imu data publication code block
  void timer_callback()
  {
    // Receive raw HighState via UDP
    bridge_.udp.Recv();
    bridge_.udp.GetRecv(bridge_.state);
    // Convert to ROS message and publish
    state_ros_ = state2rosMsg(bridge_.state);
    pub_state_->publish(state_ros_);

    if constexpr (publish_enabled) {
    // IMU message
    sensor_msgs::msg::Imu imu_msg;
    imu_msg.header.stamp = now();
    imu_msg.header.frame_id = imu_frame_;

    // Orientation quaternion
    imu_msg.orientation = tf2::toMsg(
      tf2::Quaternion(
        state_ros_.imu.quaternion[0], state_ros_.imu.quaternion[1],
        state_ros_.imu.quaternion[2], state_ros_.imu.quaternion[3]
      )
    );
    // Angular velocity
    imu_msg.angular_velocity.x = state_ros_.imu.gyroscope[0];
    imu_msg.angular_velocity.y = state_ros_.imu.gyroscope[1];
    imu_msg.angular_velocity.z = state_ros_.imu.gyroscope[2];
    // Linear acceleration
    imu_msg.linear_acceleration.x = state_ros_.imu.accelerometer[0];
    imu_msg.linear_acceleration.y = state_ros_.imu.accelerometer[1];
    imu_msg.linear_acceleration.z = state_ros_.imu.accelerometer[2];

    pub_imu_->publish(imu_msg);

    // Odometry message
    nav_msgs::msg::Odometry odom_msg;
    odom_msg.header.stamp = imu_msg.header.stamp;
    odom_msg.header.frame_id = odom_frame_;
    odom_msg.child_frame_id = link_frame_;

    // Pose
    odom_msg.pose.pose.position.x = state_ros_.position[0];
    odom_msg.pose.pose.position.y = state_ros_.position[1];
    odom_msg.pose.pose.position.z = state_ros_.position[2];
    odom_msg.pose.pose.orientation = imu_msg.orientation;
    // Twist
    odom_msg.twist.twist.linear.x = state_ros_.velocity[0];
    odom_msg.twist.twist.linear.y = state_ros_.velocity[1];
    odom_msg.twist.twist.linear.z = state_ros_.velocity[2];
    odom_msg.twist.twist.angular.z = state_ros_.yaw_speed;
    pub_odom_->publish(odom_msg);
    };
  };
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<UDPHighNode>());
  rclcpp::shutdown();
  return 0;
}
