#!/usr/bin/env python

import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    rospy.init_node('fake_scan_publisher', anonymous = True)
    prev_time = rospy.Time.now()
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size = 10)
    fake_scan = LaserScan()
    current_time = rospy.Time.now()
    fake_scan.header.stamp = current_time
    fake_scan.header.frame_id = "base_link"
    fake_scan.angle_min = (-2/3)*math.pi
    fake_scan.angle_max = (2/3)*math.pi
    fake_scan.angle_increment = (1.0/300)*math.pi
    fake_scan.scan_time = (current_time-prev_time).to_sec()
    prev_time = current_time
    fake_scan.range_min = 1.0
    fake_scan.range_max = 10.0
    angle_range = fake_scan.angle_max - fake_scan.angle_min
    num_angles = int(angle_range/fake_scan.angle_increment-1)   # 400-1
    scan_ranges = np.random.uniform(fake_scan.range_min,fake_scan.range_max,num_angles)
    fake_list = list(scan_ranges)
    fake_list.append(fake_scan.range_min)
    fake_list.append(fake_scan.range_max)
    fake_scan.ranges = fake_list
    rate = rospy.Rate(20) #20hz
    while not rospy.is_shutdown():
        rospy.loginfo(fake_scan)
        pub.publish(fake_scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
    except rospy.ROSInterruptException:
        pass