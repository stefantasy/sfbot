#!/bin/bash
killall gnome-terminal-server
source /opt/ros/kinetic/setup.bash;
source ~/sfbot_ws/devel/setup.bash;
gnome-terminal -t "播报服务" -x bash -c "roslaunch sfbot_bringup soundplay.launch ;exec bash;"

echo hello everyone i am china robot c r o s robot|rosrun sound_play say.py
