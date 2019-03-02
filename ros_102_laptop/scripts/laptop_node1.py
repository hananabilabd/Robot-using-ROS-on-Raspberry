#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#from __future__ import print_function

import sys, select, termios, tty
class Main():
    def __init__(self, parent=None):
        self.settings = termios.tcgetattr(sys.stdin)
        rospy.init_node('laptop_node1', anonymous=False)
        self.sub = rospy.Subscriber('/robot/move_speed_feedback', String, self.callback)
        self.pub = rospy.Publisher('/robot/move_speed', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.twist = Twist()

        self.moveBindings = {
                'up':(1,0,0,0),
                'down':(-1,0,0,0),
                'right':(0,0,0,1),
                'left':(0,0,0,-1),
                'stop':(0,0,0,0),
            }
        self.speedBindings={
                'w':(1,1),
                's':(0,0),
                'j':(1.1,1),
            }
        self.X = 0;self.Y=0;self.Z=0
        self.X_angular = 0;self.Y_angular=0;self.Z_angular=0
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        if key == '\x1b':
            key = sys.stdin.read(2)
            if key == '[A':
                return "up"
            elif key == '[B':
                return "down"
            elif key == '[C':
                return "right"
            elif key == '[D':
                return "left"
            else:
                return "not an arrow key!"
        return key

    def callback (self,msg):
        rospy.loginfo("from raspberr_node1: message received")
        rospy.loginfo("status :%s ", msg.data)
        self.twist.linear.x = 0;self.twist.linear.y = 0;self.twist.linear.z = 0;
        self.twist.angular.x = 0;self.twist.angular.y = 0;self.twist.angular.z = 0
        #self.pub.publish(self.twist)

    def laptop_node1_moving(self):

        speed =1
        while not rospy.is_shutdown():
            key = self.getKey()
            if (key == '\x03'):
                break
            elif key in self.moveBindings.keys():
                X = self.moveBindings[key][0]
                Y = self.moveBindings[key][1]
                Z = self.moveBindings[key][2]
            elif key in self.speedBindings.keys() :
                speed =self.speedBindings[key][0]

            self.twist.linear.x = X * speed;self.twist.linear.y = Y * speed;self.twist.linear.z = Z * speed;
            self.twist.angular.x = speed;self.twist.angular.y = 0;self.twist.angular.z = 0
            self.pub.publish(self.twist)
            self.rate.sleep()
		
if __name__== '__main__':
	try:
         m=Main()
         m.laptop_node1_moving()
	except rospy.ROSInterruptException:
    		pass