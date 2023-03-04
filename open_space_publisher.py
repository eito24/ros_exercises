#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
import math


def callback(data):
    rate = rospy.Rate(20) #20hz
    while not rospy.is_shutdown():
        fake_scan = data
        distance = max(fake_scan.ranges)
        distance_i = fake_scan.ranges.index(distance)
        angle = fake_scan.angle_min + fake_scan.angle_increment*distance_i
        pub1 = rospy.Publisher('open_space/distance', Float32, queue_size = 10)
        pub2 = rospy.Publisher('open_space/angle', Float32, queue_size = 10)
        pub1.publish(distance)
        pub2.publish(angle)
        rospy.loginfo(fake_scan)
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
