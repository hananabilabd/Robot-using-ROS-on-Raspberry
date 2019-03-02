#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#import wiringpi
import RPi.GPIO as GPIO
import time

class Main():
    def __init__(self, parent=None):
        rospy.init_node('raspberry_node2', anonymous=False)
        self.sub = rospy.Subscriber('/robot/ultrasound_sensor_feedback', String, self.callback)
        self.pub = rospy.Publisher('/robot/ultrasound_sensor_status', String, queue_size=5)
        self.rate = rospy.Rate(1)
        self.twist = Twist()
        
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

    



    def callback(self,msg):
        rospy.loginfo("Received from laptop node 2 :" + msg)
    def raspberry_node2_ultrasound(self):

        while not rospy.is_shutdown():
            self.read_distance()
            self.rate.sleep()
def read_distance():
    TRIG = 23
    ECHO = 24
    #self.pub.publish("Distance Measurement In Progress")
    print("Distance Measurement In Progress")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    #self.pub.publish("Waiting For Sensor To Settle")
    print("Waiting For Sensor To Settle")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration *17150
    distance = round(distance, 2)
    msg="Distance:"+ str(distance)+"cm"
    #self.pub.publish(msg)
    print(msg)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        while True :
            read_distance()
    except rospy.ROSInterruptException:
        pass
