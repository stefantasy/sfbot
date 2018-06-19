#!/bin/bash
killall gnome-terminal-server
source /opt/ros/kinetic/setup.bash;
source ~/sfbot_ws/devel/setup.bash;
source ~/ros_voice_system/devel/setup.bash;
gnome-terminal -t "ROS语音系统" -x bash -c "roslaunch voice_bringup voice_bringup.launch ;exec bash;"
sleep 5
gnome-terminal -t "启动底盘" -x bash -c "roslaunch sfbot_bringup mini_start.launch ;exec bash;"

