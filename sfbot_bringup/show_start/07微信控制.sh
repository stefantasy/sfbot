#!/bin/bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash
source /home/sfbot/ros_voice_system/devel/setup.bash
gnome-terminal -t "启动微信控制" -x bash -c "roslaunch sfbot_itchat sfbot_wechat.launch ;exec bash;"
