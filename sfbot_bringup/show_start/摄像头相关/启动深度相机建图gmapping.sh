#!/bin/bash
killall gnome-terminal-server 
source /opt/ros/kinetic/setup.bash;
source ~/sfbot_ws/devel/setup.bash;

gnome-terminal -t "播报服务" -x bash -c "roslaunch sfbot_bringup soundplay.launch ;exec bash;"

echo G Maping Mode|rosrun sound_play say.py

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch sfbot_bringup camera_start.launch ;exec bash;"

sleep 2.5
gnome-terminal -t "启动Gmapping建图" -x bash -c "roslaunch sfbot_nav gmapping_demo.launch ;exec bash;"

sleep 1
roslaunch sfbot_rviz gmapping_view.launch
