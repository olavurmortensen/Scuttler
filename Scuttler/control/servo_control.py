#!/usr/bin/env python

from adafruit_servokit import ServoKit

servo = ServoKit(channels=16).servo

def move(servo_id, angle):
    servo[servo_id].angle = angle

