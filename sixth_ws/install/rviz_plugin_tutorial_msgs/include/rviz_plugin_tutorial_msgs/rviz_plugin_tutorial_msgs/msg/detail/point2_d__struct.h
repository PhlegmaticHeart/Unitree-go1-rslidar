// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rviz_plugin_tutorial_msgs:msg/Point2D.idl
// generated code does not contain a copyright notice

#ifndef RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__STRUCT_H_
#define RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Point2D in the package rviz_plugin_tutorial_msgs.
typedef struct rviz_plugin_tutorial_msgs__msg__Point2D
{
  std_msgs__msg__Header header;
  double x;
  double y;
} rviz_plugin_tutorial_msgs__msg__Point2D;

// Struct for a sequence of rviz_plugin_tutorial_msgs__msg__Point2D.
typedef struct rviz_plugin_tutorial_msgs__msg__Point2D__Sequence
{
  rviz_plugin_tutorial_msgs__msg__Point2D * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rviz_plugin_tutorial_msgs__msg__Point2D__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // RVIZ_PLUGIN_TUTORIAL_MSGS__MSG__DETAIL__POINT2_D__STRUCT_H_
