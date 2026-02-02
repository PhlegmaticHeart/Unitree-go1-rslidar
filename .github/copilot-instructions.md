# AI Coding Agent Instructions for Helios16P Robot Workspace

## Project Overview
This is a ROS2 workspace integrating Robosense Helios 16P LiDAR on a Unitree Go1 robot dog for SLAM and odometry. The system combines LiDAR drivers, ICP-based odometry (KISS-ICP), and robot description for autonomous navigation.

## Architecture Components

### Core Packages
- **`rslidar_msg`**: Custom ROS2 message definitions for LiDAR data
- **`rslidar_sdk`**: LiDAR driver node publishing to `/rslidar_points`
- **`kiss_icp`**: Odometry SLAM pipeline processing pointclouds to `/kiss/pose`
- **`helios16p_cane_robot`**: Launch files and configurations
- **`go1_description`**: XACRO robot model with sensors (LiDAR, depth camera, ultrasound)
- **`vicon_receiver`**: Motion capture integration for ground truth

### Data Flow
```
LiDAR Driver → /rslidar_points → KISS-ICP → /kiss/pose → TF (odom_lidar)
                                      ↓
Robot State Publisher → TF tree (map → base_l → rslidar)
                                      ↓
RViz Visualization
```

## Critical Workflows

### Build Process
```bash
# Source ROS2 environment first
source /opt/ros/humble/setup.bash

# Build order is critical - rslidar_msg before rslidar_sdk
cd /home/ph/ws/helios16p_ws
colcon build --packages-select rslidar_msg rslidar_sdk
colcon build  # Build remaining packages
source install/setup.bash
```

### Launch Commands
```bash
# Real hardware with visualization
ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py visualize:=true

# Simulation mode with bag file
ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py simulate:=true bagfile:=your_bag_path

# Debug without KISS-ICP
ros2 launch helios16p_cane_robot helios16p_cane_robot.launch.py nokiss:=true
```

## Configuration Patterns

### Range-Based Configs
Pre-configured YAML files in `helios16p_cane_robot/configs/`:
- `mrange4.yaml` through `mrange30.yaml` for different max ranges
- Tune `data.max_range`, `mapping.voxel_size`, `mapping.max_points_per_voxel`
- Launch parameter: `setrange:=mrange10.yaml`

### Launch Parameters
```python
# Key tuning parameters (from launch file)
'data.max_range': '30.0'          # Pointcloud filtering
'mapping.voxel_size': '0.3'       # SLAM resolution
'mapping.max_points_per_voxel': '10'  # Memory efficiency
'registration.max_num_iterations': '700'  # ICP convergence
'registration.convergence_criterion': '0.0001'  # ICP precision
```

## Code Conventions

### XACRO Structure
- Main robot model: `go1_description/xacro/robot.xacro`
- Modular includes: `leg.xacro`, `helios16p_LiDAR.urdf.xacro`, `depthCamera.xacro`
- Arguments: `lidar_x_offset`, `lidar_y_offset`, `lidar_z_offset` for sensor positioning

### TF Frame Hierarchy
```
map → base_l → rslidar
      ↓
   odom_lidar (from KISS-ICP)
```

### Topic Naming
- Input: `/rslidar_points` (remappable via `pointcloud_topic` parameter)
- Output: `/kiss/pose`, `/tf` transforms
- Debug: Conditional `publish_debug_clouds` for pointcloud visualization

## Integration Points

### External Dependencies
- **ROS2 Humble**: Core middleware
- **xacro**: Robot description preprocessing
- **tf2**: Transform management
- **RViz2**: Visualization (config: `launchrviz.rviz`)

### Sensor Integration
- LiDAR mounted at configurable offset from base_link
- Static transforms defined in launch file
- Simulation mode uses ROS bag playback with `--clock` for timing

### Parameter Loading
```bash
# Override configs at runtime
ros2 param load /kiss_icp_node /path/to/config.yaml
```

## Development Workflow

### Testing Changes
1. Build modified packages: `colcon build --packages-select <package>`
2. Source environment: `source install/setup.bash`
3. Launch with debug flags: `visualize:=true nokiss:=false`
4. Monitor topics: `ros2 topic echo /kiss/pose`

### Common Issues
- **Build order**: Always build `rslidar_msg` before `rslidar_sdk`
- **TF errors**: Verify frame hierarchy and static transforms
- **Memory**: Reduce `mapping.max_points_per_voxel` for performance
- **Range tuning**: Match LiDAR config with KISS-ICP parameters

## File Organization
- **Launch files**: `helios16p_cane_robot/launch/`
- **Configs**: `helios16p_cane_robot/configs/` (YAML + RViz)
- **Robot model**: `go1_description/xacro/` (XACRO files)
- **Maps**: `maps/` directory for SLAM outputs