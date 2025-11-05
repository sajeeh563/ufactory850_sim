from setuptools import setup
import os
from glob import glob

package_name = 'ufactory850_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Install all launch files
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        # Install urdf and world files
        ('share/' + package_name + '/urdf', glob('urdf/*')),
        ('share/' + package_name + '/worlds', glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sajeeh',
    maintainer_email='your@email.com',
    description='uFactory850 simulation package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pick_and_place = ufactory850_sim.pick_and_place:main',
        ],
    },
)