#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Main():
    def __init__(self, parent=None):
        rospy.init_node('laptop_node2', anonymous=False)
        self.sub = rospy.Subscriber('/robot/ultrasound_sensor_status', String, self.callback)
        self.pub = rospy.Publisher('/robot/ultrasound_sensor_feedback', String, queue_size=10)
        self.rate = rospy.Rate(0.5)
        self.twist = Twist()


    def read_distance(self):
        self.pub.publish("acknowledge")

    def callback(self,msg):
        rospy.loginfo("Received from raspberry node 2: %s " ,msg.data)

    def laptop_node2_ultrasound(self):
        while not rospy.is_shutdown():
            self.read_distance()
            self.rate.sleep()


if __name__ == '__main__':
    try:
        m=Main()
        m.laptop_node2_ultrasound()
    except rospy.ROSInterruptException:
        pass