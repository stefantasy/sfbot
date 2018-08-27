#!/bin/bash
killall gnome-terminal-server
source /opt/ros/kinetic/setup.bash;
source ~/sfbot_ws/devel/setup.bash;

gnome-terminal -t "播报服务" -x bash -c "roslaunch sfbot_bringup soundplay.launch ;exec bash;"

echo Open C V Camshift Mode|rosrun sound_play say.py

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch sfbot_bringup camera_start.launch ;exec bash;"

sleep 2
gnome-terminal -t "启动颜色追踪follower" -x bash -c "roslaunch sfbot_apps opencv3_follower.launch color:=true ;exec bash;"

