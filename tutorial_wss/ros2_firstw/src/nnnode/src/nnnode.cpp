#include <memory>
#include <string>
#include <thread>
#include "lifecycle_msgs/msg/transition.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_lifecycle/lifecycle_node.hpp"
#include "rclcpp_lifecycle/lifecycle_publisher.hpp"



void node_info(std::shared_ptr<rclcpp::node_interfaces::NodeBaseInterface> base_interface,
               std::shared_ptr<rclcpp::node_interfaces::NodeLoggingInterface> logging_interface)
{
  RCLCPP_INFO(logging_interface->get_logger(), "Node name: %s", base_interface->get_name());
};

class SimpleNode : public rclcpp::Node
{
public:
  SimpleNode(const std::string & node_name)
  : Node(node_name)
  {}
};

class LifecycleTalker : public rclcpp_lifecycle::LifecycleNode
{
public:
  explicit LifecycleTalker(const std::string & node_name, bool intra_process_comms = false)
  : rclcpp_lifecycle::LifecycleNode(node_name,
      rclcpp::NodeOptions().use_intra_process_comms(intra_process_comms))
  {}
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::executors::SingleThreadedExecutor exe;
  auto node = std::make_shared<SimpleNode>("Simple_Node");
  auto lc_node = std::make_shared<LifecycleTalker>("Simple_LifeCycle_Node");
  rclcpp::shutdown();
  return 0;
};

