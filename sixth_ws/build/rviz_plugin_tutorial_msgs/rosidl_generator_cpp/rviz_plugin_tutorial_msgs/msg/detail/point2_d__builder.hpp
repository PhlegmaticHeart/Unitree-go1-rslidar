// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rviz_plugin_tutorial_msgs:msg/Point2D.idl
// generated code does not contain a copyright notice

#ifndef RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__BUILDER_HPP_
#define RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "rviz_plugin_tutorial_msgs/msg/detail/point2_d__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace rviz_plugin_tutorial_msgs
{

namespace msg
{

namespace builder
{

class Init_Point2D_y
{
public:
  explicit Init_Point2D_y(::rviz_plugin_tutorial_msgs::msg::Point2D & msg)
  : msg_(msg)
  {}
  ::rviz_plugin_tutorial_msgs::msg::Point2D y(::rviz_plugin_tutorial_msgs::msg::Point2D::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rviz_plugin_tutorial_msgs::msg::Point2D msg_;
};

class Init_Point2D_x
{
public:
  explicit Init_Point2D_x(::rviz_plugin_tutorial_msgs::msg::Point2D & msg)
  : msg_(msg)
  {}
  Init_Point2D_y x(::rviz_plugin_tutorial_msgs::msg::Point2D::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Point2D_y(msg_);
  }

private:
  ::rviz_plugin_tutorial_msgs::msg::Point2D msg_;
};

class Init_Point2D_header
{
public:
  Init_Point2D_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Point2D_x header(::rviz_plugin_tutorial_msgs::msg::Point2D::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Point2D_x(msg_);
  }

private:
  ::rviz_plugin_tutorial_msgs::msg::Point2D msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rviz_plugin_tutorial_msgs::msg::Point2D>()
{
  return rviz_plugin_tutorial_msgs::msg::builder::Init_Point2D_header();
}

}  // namespace rviz_plugin_tutorial_msgs

#endif  // RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__BUILDER_HPP_
