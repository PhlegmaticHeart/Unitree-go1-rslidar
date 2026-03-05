// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from unitree_nav_interfaces:srv/SetGait.idl
// generated code does not contain a copyright notice

#ifndef UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_H_
#define UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'IDLE'.
enum
{
  unitree_nav_interfaces__srv__SetGait_Request__IDLE = 0
};

/// Constant 'TROT'.
enum
{
  unitree_nav_interfaces__srv__SetGait_Request__TROT = 1
};

/// Constant 'TROT_RUNNING'.
enum
{
  unitree_nav_interfaces__srv__SetGait_Request__TROT_RUNNING = 2
};

/// Constant 'CLIMB_STAIRS'.
enum
{
  unitree_nav_interfaces__srv__SetGait_Request__CLIMB_STAIRS = 3
};

/// Constant 'TROT_OBSTACLE'.
enum
{
  unitree_nav_interfaces__srv__SetGait_Request__TROT_OBSTACLE = 4
};

/// Struct defined in srv/SetGait in the package unitree_nav_interfaces.
typedef struct unitree_nav_interfaces__srv__SetGait_Request
{
  uint8_t gait;
} unitree_nav_interfaces__srv__SetGait_Request;

// Struct for a sequence of unitree_nav_interfaces__srv__SetGait_Request.
typedef struct unitree_nav_interfaces__srv__SetGait_Request__Sequence
{
  unitree_nav_interfaces__srv__SetGait_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} unitree_nav_interfaces__srv__SetGait_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetGait in the package unitree_nav_interfaces.
typedef struct unitree_nav_interfaces__srv__SetGait_Response
{
  uint8_t structure_needs_at_least_one_member;
} unitree_nav_interfaces__srv__SetGait_Response;

// Struct for a sequence of unitree_nav_interfaces__srv__SetGait_Response.
typedef struct unitree_nav_interfaces__srv__SetGait_Response__Sequence
{
  unitree_nav_interfaces__srv__SetGait_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} unitree_nav_interfaces__srv__SetGait_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UNITREE_NAV_INTERFACES__SRV__DETAIL__SET_GAIT__STRUCT_H_
