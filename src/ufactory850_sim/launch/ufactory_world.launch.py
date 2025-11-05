from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose',
                 str('/home/sajeeh/ufactory_ws/src/ufactory850_sim/worlds/loop_channel.world'),
                 '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
    ])
