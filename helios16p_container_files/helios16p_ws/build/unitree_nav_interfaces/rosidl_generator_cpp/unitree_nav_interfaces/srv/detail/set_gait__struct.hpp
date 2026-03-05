// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from unitree_nav_interfaces:srv/SetGait.idl
// generated code does not contain a copyright notice

#ifndef UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_HPP_
#define UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__unitree_nav_interfaces__srv__SetGait_Request __attribute__((deprecated))
#else
# define DEPRECATED__unitree_nav_interfaces__srv__SetGait_Request __declspec(deprecated)
#endif

namespace unitree_nav_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetGait_Request_
{
  using Type = SetGait_Request_<ContainerAllocator>;

  explicit SetGait_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gait = 0;
    }
  }

  explicit SetGait_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gait = 0;
    }
  }

  // field types and members
  using _gait_type =
    uint8_t;
  _gait_type gait;

  // setters for named parameter idiom
  Type & set__gait(
    const uint8_t & _arg)
  {
    this->gait = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t IDLE =
    0u;
  static constexpr uint8_t TROT =
    1u;
  static constexpr uint8_t TROT_RUNNING =
    2u;
  static constexpr uint8_t CLIMB_STAIRS =
    3u;
  static constexpr uint8_t TROT_OBSTACLE =
    4u;

  // pointer types
  using RawPtr =
    unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__unitree_nav_interfaces__srv__SetGait_Request
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__unitree_nav_interfaces__srv__SetGait_Request
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetGait_Request_ & other) const
  {
    if (this->gait != other.gait) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetGait_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetGait_Request_

// alias to use template instance with default allocator
using SetGait_Request =
  unitree_nav_interfaces::srv::SetGait_Request_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t SetGait_Request_<ContainerAllocator>::IDLE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t SetGait_Request_<ContainerAllocator>::TROT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t SetGait_Request_<ContainerAllocator>::TROT_RUNNING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t SetGait_Request_<ContainerAllocator>::CLIMB_STAIRS;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t SetGait_Request_<ContainerAllocator>::TROT_OBSTACLE;
#endif  // __cplusplus < 201703L

}  // namespace srv

}  // namespace unitree_nav_interfaces


#ifndef _WIN32
# define DEPRECATED__unitree_nav_interfaces__srv__SetGait_Response __attribute__((deprecated))
#else
# define DEPRECATED__unitree_nav_interfaces__srv__SetGait_Response __declspec(deprecated)
#endif

namespace unitree_nav_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetGait_Response_
{
  using Type = SetGait_Response_<ContainerAllocator>;

  explicit SetGait_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit SetGait_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__unitree_nav_interfaces__srv__SetGait_Response
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__unitree_nav_interfaces__srv__SetGait_Response
    std::shared_ptr<unitree_nav_interfaces::srv::SetGait_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetGait_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetGait_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetGait_Response_

// alias to use template instance with default allocator
using SetGait_Response =
  unitree_nav_interfaces::srv::SetGait_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace unitree_nav_interfaces

namespace unitree_nav_interfaces
{

namespace srv
{

struct SetGait
{
  using Request = unitree_nav_interfaces::srv::SetGait_Request;
  using Response = unitree_nav_interfaces::srv::SetGait_Response;
};

}  // namespace srv

}  // namespace unitree_nav_interfaces

#endif  // UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_HPP_
