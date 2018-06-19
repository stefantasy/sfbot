#!/bin/bash
killall gnome-terminal-server
source /opt/ros/kinetic/setup.bash;
source ~/sfbot_ws/devel/setup.bash;

gnome-terminal -t "播报服务" -x bash -c "roslaunch sfbot_bringup soundplay.launch ;exec bash;"

echo P C L Follow Mode|rosrun sound_play say.py

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch sfbot_bringup camera_start.launch ;exec bash;"

sleep 2.5
gnome-terminal -t "启动PCL点云追踪follower" -x bash -c "roslaunch sfbot_apps follower2.launch ;exec bash;"


