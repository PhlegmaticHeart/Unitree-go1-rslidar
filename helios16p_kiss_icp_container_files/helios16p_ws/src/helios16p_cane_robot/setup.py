from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'helios16p_cane_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'configs'), glob('configs/*.rviz')),
        (os.path.join('share', package_name, 'configs'), glob('configs/*.yaml')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf.xacro')),
        # (os.path.join('share', package_name, 'go1_description', 'xacro'), glob('go1_description/xacro/*.xacro')),
        # (os.path.join('share', package_name, 'go1_description', 'meshes'), glob('go1_description/meshes/*')),
#        (os.path.join('share', 'vicon_receiver', 'launch'), glob('vicon_receiver/launch/*.launch.py')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gabriele Barletta',
    maintainer_email='Gabriele.Barletta03@gmail.com',
    description='This package hs the aim of organizing and configuring all nodes related to Lidar Helios 16P Robosense functioning, accordingly to Links Foundation requirements.',
    license='GNU GPL',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [],
    },
)

