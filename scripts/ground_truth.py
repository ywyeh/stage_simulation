#!/usr/bin/python3
import rospy
from nav_msgs.msg import Odometry

class FixGroundTruth:
    def __init__(self):
        self.ground_truth_sub = rospy.Subscriber("base_pose_ground_truth", Odometry, self.ground_truth_sub_callback)
        self.ground_truth_pub = rospy.Publisher("ground_truth", Odometry, queue_size=10)

    def ground_truth_sub_callback(self, odom):
        odom.header.frame_id = "map"
        self.ground_truth_pub.publish(odom)


if __name__ == '__main__':
    rospy.init_node('ground_truth_pub', anonymous=True)
    fix_ground_truth = FixGroundTruth()
    rospy.spin()
    