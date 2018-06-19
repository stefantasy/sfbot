#!/bin/bash
killall gnome-terminal-server
source ~/catkin_ws/devel/setup.bash;

gnome-terminal -t "播报服务" -x bash -c "roslaunch mx_bringup mx_soundplay.launch ;exec bash;"

echo Open C V Camshift Tracking Mode|rosrun sound_play say.py

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch mx_bringup rbc_camera_start.launch ;exec bash;"

sleep 2
gnome-terminal -t "启动颜色追踪tracker" -x bash -c "roslaunch mx_apps opencv3_tracker.launch color:=true ;exec bash;"

