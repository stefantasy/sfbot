#!/bin/bash

killall gnome-terminal-server
source /opt/ros/kinetic/setup.bash;
source ~/catkin_ws/devel/setup.bash;

gnome-terminal -t "播报服务" -x bash -c "roslaunch mx_bringup mx_soundplay.launch ;exec bash;"

echo hello i am RBC bot|rosrun sound_play say.py

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch mx_bringup rbc_camera_start.launch ;exec bash;"
