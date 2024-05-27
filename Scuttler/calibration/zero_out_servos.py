#!/usr/bin/env python

from time import sleep
from adafruit_servokit import ServoKit

if __name__ == '__main__':
    servo = ServoKit(channels=16)
    print('Setting all servo angles to 0.')
    print('Servo number:')
    for i in range(12):
        print(i)
        servo.servo[i].angle = 0
        sleep(0.5)
