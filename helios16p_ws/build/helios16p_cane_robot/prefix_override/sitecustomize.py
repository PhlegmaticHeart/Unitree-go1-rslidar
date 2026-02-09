import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ph/treasure/dockerBENCH/helios16p_ws/install/helios16p_cane_robot'
