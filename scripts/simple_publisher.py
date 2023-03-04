#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32

def simple_publisher():
    pub = rospy.Publisher('my_random_float', Float32, queue_size = 10)
    rospy.init_node('simple_publisher', anonymous = True)
    rate = rospy.Rate(20) #20hz
    while not rospy.is_shutdown():
        random_float = random.uniform(0,10)
        rospy.loginfo(random_float)
        pub.publish(random_float)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
