#!/usr/bin/env python

# Copyright (c) 2017-2018 williamar. 
# All right reserved.

import rospy, actionlib

from control_msgs.msg import FollowJointTrajectoryAction
from trajectory_msgs.msg import JointTrajectory
from diagnostic_msgs.msg import *
from math import pi as PI, degrees, radians
from joints import Joint

class FollowController:

    def __init__(self, name):
        self.name = name
        
        rospy.init_node(self.name)
        

        # rates
        self.rate = 10.0
        
        # Arm jonits
        self.arm_base_to_arm_round_joint_stevo0=Joint('arm_base_to_arm_round_joint_stevo0',0,1.5797,-1.5707,130,0,False)
        self.shoulder_2_to_arm_joint_stevo1=Joint('shoulder_2_to_arm_joint_stevo1',1,1.5707,-0.1899,115,45,False)
        self.big_arm_round_to_joint_stevo2=Joint('big_arm_round_to_joint_stevo2',2,2.5891,1,100,20,False)
        self.arm_joint_stevo2_to_arm_joint_stevo3=Joint('arm_joint_stevo2_to_arm_joint_stevo3',3,1.5707,-1.5707,130,0,False)
        self.wrist_to_arm_joint_stevo4=Joint('wrist_to_arm_joint_stevo4',4,1.5707,-1.5707,130,0,False)
        self.arm_joint_stevo4_to_arm_joint_stevo5=Joint('arm_joint_stevo4_to_arm_joint_stevo5',5,1.5707,-1.5707,130,0,True)
        
        
        
        self.joints=[self.arm_base_to_arm_round_joint_stevo0,
        self.shoulder_2_to_arm_joint_stevo1,
        self.big_arm_round_to_joint_stevo2,
        self.arm_joint_stevo2_to_arm_joint_stevo3,
        self.wrist_to_arm_joint_stevo4,
        self.arm_joint_stevo4_to_arm_joint_stevo5]
        
        # action server
        self.server = actionlib.SimpleActionServer('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction, execute_cb=self.actionCb, auto_start=False)
        self.server.start()
        rospy.spin()
        rospy.loginfo("Started FollowController")


    def actionCb(self, goal):
	print("****************actionCb*********************")    
        rospy.loginfo(self.name + ": Action goal recieved.")
        traj = goal.trajectory

        if set(self.joints) != set(traj.joint_names):
            for j in self.joints:
                if j.name not in traj.joint_names:
                    msg = "Trajectory joint names does not match action controlled joints." + str(traj.joint_names)
                    rospy.logerr(msg)
                    self.server.set_aborted(text=msg)
                    return
            rospy.logwarn("Extra joints in trajectory")

        if not traj.points:
            msg = "Trajectory empy."
            rospy.logerr(msg)
            self.server.set_aborted(text=msg)
            return

        try:
            indexes = [traj.joint_names.index(joint.name) for joint in self.joints]
        except ValueError as val:
            msg = "Trajectory invalid."
            rospy.logerr(msg)
            self.server.set_aborted(text=msg)
            return

        if self.executeTrajectory(traj):   
            self.server.set_succeeded()
        else:
            self.server.set_aborted(text="Execution failed.")

        rospy.loginfo(self.name + ": Done.")     

    def executeTrajectory(self, traj):
        rospy.loginfo("Executing trajectory")
        rospy.logdebug(traj)
        # carry out trajectory
        try:
            indexes = [traj.joint_names.index(joint.name) for joint in self.joints]
        except ValueError as val:
            rospy.logerr("Invalid joint in trajectory.")
            return False

        # get starting timestamp, MoveIt uses 0, need to fill in
        start = traj.header.stamp
        if start.secs == 0 and start.nsecs == 0:
            start = rospy.Time.now()

        r = rospy.Rate(self.rate)
	for point in traj.points:            
            desired = [ point.positions[k] for k in indexes ]
            for i in indexes:
                #self.joints[i].position=desired[i]
                self.joints[i].setCurrentPosition(desired[i])

            while rospy.Time.now() + rospy.Duration(0.01) < start:
                rospy.sleep(0.01)
        return True
    

if __name__=='__main__':
    try:
        rospy.loginfo("start followController...")
        FollowController('follow_Controller')
    except rospy.ROSInterruptException:
        rospy.loginfo('Failed to start followController...')
        

