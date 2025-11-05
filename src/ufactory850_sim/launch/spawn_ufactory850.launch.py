from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    world_path = os.path.join(
        os.getenv('HOME'),
        'ufactory_ws/src/ufactory850_sim/worlds/loop_channel.world'
    )
    urdf_path = os.path.join(
        os.getenv('HOME'),
        'ufactory_ws/src/ufactory850_sim/urdf/ufactory850.urdf.xacro'
    )

    return LaunchDescription([
        # Start Gazebo with the custom world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # Spawn the robot into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'ufactory850',
                '-file', urdf_path,
                '-x', '0', '-y', '0', '-z', '0.32'
            ],
            output='screen'
        ),
    ])
