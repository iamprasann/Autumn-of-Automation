#!/usr/bin/env python
import rospy
import math
from beginner_tutorials.msg import quaternions
from beginner_tutorials.msg import eulerangles
class q_to_e(object):
	def __init__(self):
		self.angles=eulerangles()
        self.angles.pitch=0
		self.angles.yaw=0
		self.angles.roll=0
		rospy.init_node('q_to_e', anonymous=True)
		rospy.Subscriber('listener', quaternions, self.convert)
		self.pub=rospy.Publisher('speaker', eulerangles)

	def convert(self, msg):
		(x,y,z,w)=(msg.x, msg.y, msg.z, msg.w)
        self.angles.pitch=math.atan2(2*x*y+2*w*z, 1-(2*y*y+2*z*z))
        self.angles.yaw=math.asin(2*x*z-2*y*w)
		self.angles.roll=math.atan2(2*x*w+2*y*z, 1-(2*w*w+2*z*z))

    def run(self):
		rate=rospy.Rate(1)
		while not rospy.is_shutdown():
			rospy.loginfo(self.angles)
			self.pub.publish(self.angles)
			rate.sleep()

if __name__=='__main__':
	try:
		x=q_to_e()
		x.run()
	except rospy.ROSInterruptException:
		pass
