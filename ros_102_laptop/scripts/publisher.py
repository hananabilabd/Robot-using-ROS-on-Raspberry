#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def simplePublisher():
	pub = rospy.Publisher('/test_topic_1', UInt16, queue_size=10)
	rospy.init_node('node_1', anonymous=False)
	rate = rospy.Rate(0.6) # 1hz

	# The string to be published on the topic.
	topic1_content = "my first ROS topic"
	count =0
	while not rospy.is_shutdown():
		
    		pub.publish(count)
    		rate.sleep()
		count +=1
		if (count == 11):
			count =0
if __name__== '__main__':
	
	try:
    		simplePublisher()
	except rospy.ROSInterruptException:
    		pass
