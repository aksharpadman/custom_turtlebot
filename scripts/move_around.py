#!/usr/bin/env python
import rospy
from  geometry_msgs.msg import Twist

def main():
    cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move_around', anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        twist = Twist()        
        twist.linear.x = 1
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        cmd_vel_publisher.publish((twist))
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass