from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory("gazebo_ros")
    pkg_my_bot = get_package_share_directory("my_bot")

    world = os.path.join(pkg_my_bot, "worlds", "empty.world")
    robot = os.path.join(pkg_my_bot, "urdf", "robot.urdf")

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(pkg_gazebo_ros, "launch", "gazebo.launch.py")
                ),
                launch_arguments={"world": world}.items(),
            ),
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py",
                arguments=["-entity", "my_bot", "-file", robot],
                output="screen",
            ),
        ]
    )
