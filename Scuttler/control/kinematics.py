#!/usr/bin/env python

from math import atan2, pi, sqrt, cos, sin

L1 = 35
L2 = 61

def isOutOfRange(q_deg):
    return q_deg < 0 or q_deg > 180

def throwIfOutOfRange(q_deg):
    if isOutOfRange(q_deg):
        raise ValueError('Input angle out of range: %d' %(q_deg))

def rad2deg(rad):
    return rad * 180 / pi

def deg2rad(deg):
    return deg * pi / 180

def fk_left(q1_deg, q2_deg):
    throwIfOutOfRange(q1_deg)
    throwIfOutOfRange(q2_deg)
    reach = L1 + cos(deg2rad(q2_deg)) * L2
    x = cos(deg2rad(q1_deg)) * reach
    y = sin(deg2rad(q1_deg)) * reach
    z = sin(deg2rad(q2_deg)) * L2
    return (x, y, z)

def fk_right(q1_deg, q2_deg):
    throwIfOutOfRange(q1_deg)
    throwIfOutOfRange(q2_deg)
    reach = L1 + sin(deg2rad(q2_deg)) * L2
    x = sin(deg2rad(q1_deg)) * reach
    y = cos(deg2rad(q1_deg)) * reach
    z = cos(deg2rad(q2_deg)) * L2
    return (x, y, z)

def ik_left(x, y, z):
    q1_deg = rad2deg(atan2(y, x))
    q2_deg = rad2deg(atan2(z, sqrt(x**2 + y**2) - L1))
    return (q1_deg, q2_deg)

def ik_right(x, y, z):
    q1_deg = rad2deg(atan2(x, y))
    q2_deg = rad2deg(atan2(sqrt(x**2 + y**2) - L1, z))
    return (q1_deg, q2_deg)
