import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/admin/bench/lab/STAGING_helios16p_kiss_legged_bench_cyclone_container_files/helios16p_ws/install/helios16p_cane_robot'
