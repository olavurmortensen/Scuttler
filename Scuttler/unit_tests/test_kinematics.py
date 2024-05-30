#!/usr/bin/env python

from Scuttler.control import kinematics
import pytest

def test_leftForwardKinematicsReturnsValues():
    (x, y, z) = kinematics.fk_left(0, 0);
    assert x is not None
    assert y is not None
    assert z is not None

def test_rightForwardKinematicsReturnsValues():
    (x, y, z) = kinematics.fk_right(0, 0);
    assert x is not None
    assert y is not None
    assert z is not None

def test_fkLeftThrowOnAnglesOutOfRange():
    with pytest.raises(ValueError):
        (x, y, z) = kinematics.fk_left(-1.0, 0)
    with pytest.raises(ValueError):
        (x, y, z) = kinematics.fk_left(0, -1.0)

def test_fkRightThrowOnAnglesOutOfRange():
    with pytest.raises(ValueError):
        (x, y, z) = kinematics.fk_right(-1.0, 0)
    with pytest.raises(ValueError):
        (x, y, z) = kinematics.fk_right(0, -1.0)

def test_leftInverseKinematicsReturnsValues():
    (q1, q2) = kinematics.ik_left(0, 0, 0)
    assert q1 is not None
    assert q2 is not None

def test_rightInverseKinematicsReturnsValues():
    (q1, q2) = kinematics.ik_right(0, 0, 0)
    assert q1 is not None
    assert q2 is not None

def test_leftInverseAndForwardKinematicsCompatible():
    q1_expected = 10
    q2_expected = 90
    (x, y, z) = kinematics.fk_left(q1_expected, q2_expected);
    (q1_result, q2_result) = kinematics.ik_left(x, y, z)
    assert pytest.approx(q1_result, 1e-10) == q1_expected

def test_rightInverseAndForwardKinematicsCompatible():
    q1_expected = 10
    q2_expected = 90
    (x, y, z) = kinematics.fk_right(q1_expected, q2_expected);
    (q1_result, q2_result) = kinematics.ik_right(x, y, z)
    assert pytest.approx(q1_result, 1e-10) == q1_expected
