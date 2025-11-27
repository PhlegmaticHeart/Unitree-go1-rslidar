import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ph/ws/lidar_ws_principale/install/helios16p_cane_robot'
