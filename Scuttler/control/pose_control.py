#!/usr/bin/env python

from Scuttler.control import anatomy
from Scuttler.control import kinematics
#from Scuttler.control import servo_control

standing_pose = dict({
    anatomy.Leg.FrontLeft:       (42.84297230866542, -15.593566667845373, -60.07327293374469),
    anatomy.Leg.MiddleLeft:      (44.89988572686018, -7.917061284372356, -60.07327293374469) ,
    anatomy.Leg.BackLeft:        (44.89988572686018, 7.917061284372356, -60.07327293374469),
    anatomy.Leg.BackRight:       (48.37897522874282, -27.931614371432897, -57.32124986794041),
    anatomy.Leg.MiddleRight:     (55.8632287428658, 0.0, -57.32124986794041),
    anatomy.Leg.FrontRight:      (55.65065229192932, 4.868801193366795, -57.32124986794041)
    })

pose_types = dict({
    anatomy.Pose.Standing: standing_pose
    })


def goTo(pose_type):
    pose = pose_types[pose_type]

    (x, y, z) = pose[anatomy.Leg.FrontLeft]
    (q1, q2) = kinematics.inverseKinematics(x, y, z)
    #servo_control.move(Joint.FrontLeftHip, q1)
    #servo_control.move(Joint.FrontLeftKnee, q2)
    print(anatomy.Joint.FrontLeftHip, q1)
    print(anatomy.Joint.FrontLeftKnee, q2)

    (x, y, z) = pose[anatomy.Leg.FrontRight]
    (q1, q2) = kinematics.inverseKinematics(x, y, z)
    #servo_control.move(Joint.FrontLeftHip, q1)
    #servo_control.move(Joint.FrontLeftKnee, q2)
    print(anatomy.Joint.FrontRightHip, q1)
    print(anatomy.Joint.FrontRightKnee, q2)

if __name__ == '__main__':
    goTo(anatomy.Pose.Standing)
