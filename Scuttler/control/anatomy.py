#!/usr/bin/env python

from enum import Enum

class Pose(Enum):
    Standing = 0

class Joint(Enum):
    FrontLeftHip = 0  # Servo number 0, pin 0 on PWM controls
    FrontLeftKnee = 1
    MiddleLeftHip = 2
    MiddleLeftKnee = 3
    HindLeftHip = 4
    HindLeftKnee = 5
    FrontRightHip = 6
    FrontRightKnee = 7
    MiddleRightHip = 8
    MiddleRightKnee = 9
    HindRightHip = 10
    HindRightKnee = 11

class Leg(Enum):
    FrontLeft = 0
    MiddleLeft = 1
    BackLeft = 2
    BackRight = 3
    MiddleRight = 4
    FrontRight = 5
