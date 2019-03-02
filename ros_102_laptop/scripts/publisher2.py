#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
def simplePublisher():
	t = Twist()
	t.linear.x=1
	t.linear.y=0
	t.linear.z=0
	t.angular.x=0
	t.angular.y=0
	t.angular.z=0
	pub = rospy.Publisher('/vel_msg_1', Twist, queue_size=10)
	rospy.init_node('node_1', anonymous=False)
	rate = rospy.Rate(0.6) # 1hz

	# The string to be published on the topic.
	topic1_content = "my first ROS topic"
	count =0
	while not rospy.is_shutdown():
		
    		pub.publish(t)
    		rate.sleep()
		count +=1
		if (count == 11):
			count =0
if __name__== '__main__':
	
	try:
    		simplePublisher()
	except rospy.ROSInterruptException:
    		pass
