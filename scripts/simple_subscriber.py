#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import math


def callback(data):
    random_float_log = math.log(data.data)
    pub = rospy.Publisher('random_float_log', Float32, queue_size = 10)
    pub.publish(random_float_log)
    rospy.loginfo(random_float_log)

def simple_subscriber(): 
    rospy.init_node('simple_subscriber', anonymous=True)

    rospy.Subscriber('my_random_float', Float32, callback)

    rospy.spin()
if __name__ == '__main__':
    try:
        simple_subscriber()
    except rospy.ROSInterruptException:
        pass
