#!/usr/bin/env python

from Scuttler.control import kinematics
import pytest

def test_forwardKinematicsReturnsValues():
    (x, y, z) = kinematics.forwardKinematics(0, 0);
    assert x is not None
    assert y is not None
    assert z is not None

def test_inverseKinematicsReturnsValues():
    (q1, q2) = kinematics.inverseKinematics(0, 0, 0)
    assert q1 is not None
    assert q2 is not None

def test_inverseAndForwardKinematicsCompatible():
    q1_expected = 10
    q2_expected = 90
    (x, y, z) = kinematics.forwardKinematics(q1_expected, q2_expected);
    (q1_result, q2_result) = kinematics.inverseKinematics(x, y, z)
    assert pytest.approx(q1_result, 1e-10) == q1_expected
    assert pytest.approx(q2_result, 1e-10) == q2_expected
