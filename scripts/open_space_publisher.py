#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from msg import OpenSpace
import math


def callback(data):
    rate = rospy.Rate(20) #20hz
    while not rospy.is_shutdown():
        fake_scan = data
        distance = max(fake_scan.ranges)
        distance_i = fake_scan.ranges.index(distance)
        angle = fake_scan.angle_min + fake_scan.angle_increment*distance_i
        open_space = OpenSpace()
        open_space.angle = angle
        open_space.distance = distance
        #Question 4 Material
        """ pub1 = rospy.Publisher('open_space/distance', Float32, queue_size = 10)
        pub2 = rospy.Publisher('open_space/angle', Float32, queue_size = 10)
        pub1.publish(distance)
        pub2.publish(angle) """
        pub = rospy.Publisher('open_space', OpenSpace, queue_size = 10)
        pub.publish(open_space)
        rospy.loginfo(open_space)
        rate.sleep()


def open_space_publisher(): 
    rospy.init_node('open_space_publisher', anonymous=True)

    rospy.Subscriber('fake_scan', LaserScan, callback)

    rospy.spin()
    
if __name__ == '__main__':
    try:
        open_space_publisher()
    except rospy.ROSInterruptException:
        pass
