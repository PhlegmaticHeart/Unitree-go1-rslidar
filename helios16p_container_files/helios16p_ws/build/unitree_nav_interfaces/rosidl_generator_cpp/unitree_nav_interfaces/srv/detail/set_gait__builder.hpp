// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from unitree_nav_interfaces:srv/SetGait.idl
// generated code does not contain a copyright notice

#ifndef UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__BUILDER_HPP_
#define UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "unitree_nav_interfaces/srv/detail/set_gait__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace unitree_nav_interfaces
{

namespace srv
{

namespace builder
{

class Init_SetGait_Request_gait
{
public:
  Init_SetGait_Request_gait()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::unitree_nav_interfaces::srv::SetGait_Request gait(::unitree_nav_interfaces::srv::SetGait_Request::_gait_type arg)
  {
    msg_.gait = std::move(arg);
    return std::move(msg_);
  }

private:
  ::unitree_nav_interfaces::srv::SetGait_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::unitree_nav_interfaces::srv::SetGait_Request>()
{
  return unitree_nav_interfaces::srv::builder::Init_SetGait_Request_gait();
}

}  // namespace unitree_nav_interfaces


namespace unitree_nav_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::unitree_nav_interfaces::srv::SetGait_Response>()
{
  return ::unitree_nav_interfaces::srv::SetGait_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace unitree_nav_interfaces

#endif  // UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__BUILDER_HPP_
