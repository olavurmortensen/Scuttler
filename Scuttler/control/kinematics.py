#!/usr/bin/env python

import time
from math import atan2, pi, sqrt
from adafruit_servokit import ServoKit

L1 = 35
L2 = 61

def q1_rad(x, y, z):
    return atan2(y, x)

def q2_rad(x, y, z):
    return atan2(z, sqrt(x**2 + y**2) - L1)
        
#class DriveController():
#    def __init__(self):
#        self.kinematics = Kinematics(L1=35)
#        servo = ServoKit(channels=8)
#        self.rad2deg = 180.0 / pi
#
#    def move_to(x, y, z):
#        q1_deg = self.kinematics.q1_rad(x, y, z)
#        q2_deg = self.kinematics.q2_rad(x, y, z)
#        servo.servo[0].angle = q1_deg
#        servo.servo[1].angle = q2_deg


if __name__ == '__main__':
    servo = ServoKit(channels=8)
    rad2deg = 180.0 / pi

    print('Leg outreached:')
    (x, y, z) = L1 + L2, 0, 0
    q1 = rad2deg * q1_rad(x, y, z)
    q2 = rad2deg * q2_rad(x, y, z)
    print('(x, y, z) = ', x, y, z)
    print('(q1, q2) = ', q1, q2)

    servo.servo[0].angle = q1
    servo.servo[1].angle = q2

    time.sleep(1)

    print('Leg bent at 90 deg:')
    (x, y, z) = (L1, 0, L2)
    q1 = rad2deg * q1_rad(x, y, z)
    q2 = rad2deg * q2_rad(x, y, z)
    print('(x, y, z) = ', x, y, z)
    print('(q1, q2) = ', q1, q2)

    servo.servo[0].angle = q1
    servo.servo[1].angle = q2
