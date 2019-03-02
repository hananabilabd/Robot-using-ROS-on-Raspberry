#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
def callback (msg):
	rospy.loginfo("Received a /cmd_vel message!")
	rospy.loginfo("Linear Components : [%f ,%f ,%f ]"% (msg.linear.x,msg.linear.y,msg.linear.z))
	rospy.loginfo("Angular Components : [%f ,%f ,%f ]"% (msg.angular.x,msg.angular.y,msg.angular.z))
def subscriber():
	rospy.init_node('subscriber',anonymous =True)
	rospy.Subscriber('/vel_msg_1',Twist ,callback)
	rospy.spin()
	
if __name__== '__main__':
	subscriber()

