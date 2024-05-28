#!/usr/bin/env python3

from Scuttler.control import servo_compensation
import pytest

def test_compensationReturnsValue():
    q_compensated = servo_compensation.compensate(0, 0)
    assert q_compensated is not None

def test_throwsWhenBadServoNumber():
    with pytest.raises(ValueError):
        q_compensated = servo_compensation.compensate(-1, 0)

def test_uncalibratedServoReturnsSameAsInput():
    angle = 1.2
    q_compensated = servo_compensation.compensate(0, angle)
    assert pytest.approx(q_compensated, 1e-12) == angle
