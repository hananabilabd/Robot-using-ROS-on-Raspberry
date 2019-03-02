#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
from std_msgs.msg import String
# from __future__ import print_function
import wiringpi
import time
#import sys, select, termios, tty
#settings = termios.tcgetattr(sys.stdin)
class Main():
    def __init__(self, parent=None):
        rospy.init_node('raspberry_node1', anonymous=False)
        self.sub = rospy.Subscriber('/robot/move_speed', Twist, self.callback)
        self.pub = rospy.Publisher('/robot/move_speed_feedback', String, queue_size=10)
        self.rate = rospy.Rate(10)
        self.moveBindings = {
            'up': (1, 0, 0, 0),
            'down': (-1, 0, 0, 0),
            'right': (0, 0, 0, 1),
            'left': (0, 0, 0, -1),
            'dg': (1, 0, 0, 1),
        }
        self.speedBindings = {
            'w': (1, 1),
            's': (0.2, 0.4),
            'j': (1.1, 1),
        }

        self.X=0 ; self.Y=0 ; self.Z=0 ; self.X_angular =0;  self.Y_angular =0;  self.Z_angular=0

    def callback(self,msg):
        rospy.loginfo("From Raspberry_node1 :Received from laptop node 1")
        rospy.loginfo("Linear Components : [%f ,%f ,%f ]"% (msg.linear.x,msg.linear.y,msg.linear.z))
        rospy.loginfo("Angular Components : [%f ,%f ,%f ]"% (msg.angular.x,msg.angular.y,msg.angular.z))
        self.X=msg.linear.x ;self.Y= msg.linear.y ;self.Z= msg.linear.z
        self.X_angular =msg.angular.x;self.Y_angular=msg.angular.y ; self.Z_angular=msg.angular.z


    def raspberry_node1_moving(self):
        wiringpi.wiringPiSetup()
        wiringpi.pinMode(1, 1) ;wiringpi.pinMode(2, 1);wiringpi.pinMode(3, 1);wiringpi.pinMode(4, 1)
        #wiringpi.softPwmCreate(2, 0, 100);wiringpi.softPwmCreate(3, 0, 100);wiringpi.softPwmCreate(4, 0, 100)
        
        while not rospy.is_shutdown():
            if self.X ==1:
                wiringpi.digitalWrite(1, 1)
                wiringpi.digitalWrite(2, 0)
                wiringpi.digitalWrite(3, 1)
                wiringpi.digitalWrite(4, 0)
                self.pub.publish("From Raspberry_node1: Forward Done with success")
           
            elif self.X ==-1 :
                wiringpi.digitalWrite(1, 0)
                wiringpi.digitalWrite(2, 1)
                self.pub.publish("From Raspberry_node1: Backward Done with success")
                #print("hi")
            if self.X_angular == 1 :
                #wiringpi.softPwmWrite(1, 100)  # Change PWM duty cycle
                self.pub.publish("From Raspberry_node1: Done with success")
            self.rate.sleep()
      


if __name__ == '__main__':
    try:
        m=Main()
        m.raspberry_node1_moving()
    except rospy.ROSInterruptException:
        pass