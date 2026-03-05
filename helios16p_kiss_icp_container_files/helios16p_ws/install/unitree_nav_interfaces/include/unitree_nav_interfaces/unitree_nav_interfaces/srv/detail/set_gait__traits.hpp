// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from unitree_nav_interfaces:srv/SetGait.idl
// generated code does not contain a copyright notice

#ifndef UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__TRAITS_HPP_
#define UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "unitree_nav_interfaces/srv/detail/set_gait__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace unitree_nav_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetGait_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: gait
  {
    out << "gait: ";
    rosidl_generator_traits::value_to_yaml(msg.gait, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetGait_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: gait
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gait: ";
    rosidl_generator_traits::value_to_yaml(msg.gait, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetGait_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace unitree_nav_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use unitree_nav_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const unitree_nav_interfaces::srv::SetGait_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  unitree_nav_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use unitree_nav_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const unitree_nav_interfaces::srv::SetGait_Request & msg)
{
  return unitree_nav_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<unitree_nav_interfaces::srv::SetGait_Request>()
{
  return "unitree_nav_interfaces::srv::SetGait_Request";
}

template<>
inline const char * name<unitree_nav_interfaces::srv::SetGait_Request>()
{
  return "unitree_nav_interfaces/srv/SetGait_Request";
}

template<>
struct has_fixed_size<unitree_nav_interfaces::srv::SetGait_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<unitree_nav_interfaces::srv::SetGait_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<unitree_nav_interfaces::srv::SetGait_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace unitree_nav_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetGait_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetGait_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetGait_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace unitree_nav_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use unitree_nav_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const unitree_nav_interfaces::srv::SetGait_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  unitree_nav_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use unitree_nav_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const unitree_nav_interfaces::srv::SetGait_Response & msg)
{
  return unitree_nav_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<unitree_nav_interfaces::srv::SetGait_Response>()
{
  return "unitree_nav_interfaces::srv::SetGait_Response";
}

template<>
inline const char * name<unitree_nav_interfaces::srv::SetGait_Response>()
{
  return "unitree_nav_interfaces/srv/SetGait_Response";
}

template<>
struct has_fixed_size<unitree_nav_interfaces::srv::SetGait_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<unitree_nav_interfaces::srv::SetGait_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<unitree_nav_interfaces::srv::SetGait_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<unitree_nav_interfaces::srv::SetGait>()
{
  return "unitree_nav_interfaces::srv::SetGait";
}

template<>
inline const char * name<unitree_nav_interfaces::srv::SetGait>()
{
  return "unitree_nav_interfaces/srv/SetGait";
}

template<>
struct has_fixed_size<unitree_nav_interfaces::srv::SetGait>
  : std::integral_constant<
    bool,
    has_fixed_size<unitree_nav_interfaces::srv::SetGait_Request>::value &&
    has_fixed_size<unitree_nav_interfaces::srv::SetGait_Response>::value
  >
{
};

template<>
struct has_bounded_size<unitree_nav_interfaces::srv::SetGait>
  : std::integral_constant<
    bool,
    has_bounded_size<unitree_nav_interfaces::srv::SetGait_Request>::value &&
    has_bounded_size<unitree_nav_interfaces::srv::SetGait_Response>::value
  >
{
};

template<>
struct is_service<unitree_nav_interfaces::srv::SetGait>
  : std::true_type
{
};

template<>
struct is_service_request<unitree_nav_interfaces::srv::SetGait_Request>
  : std::true_type
{
};

template<>
struct is_service_response<unitree_nav_interfaces::srv::SetGait_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__TRAITS_HPP_
