#!/usr/bin/env python

n_servos = 12
servo_ids = range(n_servos)
offset_rad = [0] * n_servos
orientation = [1] * n_servos

def compensate(servo_id, angle_rad):
    if(servo_id not in servo_ids):
        raise ValueError('Servo ID out-of-range: %d' %(servo_id))
    return orientation[servo_id] * angle_rad + offset_rad[servo_id]
