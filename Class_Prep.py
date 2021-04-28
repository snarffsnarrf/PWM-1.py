import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2


class ShotType:
    def __init__(self, m1, m2, s1, s2, direction, description):
        self.m1 = m1
        self.m2 = m2
        self.s1 = s1
        self.s2 = s2
        self.direction = direction
        self.description = description


def pwm(pin, freq):
    GPIO.PWM(pin, freq)


pwm(11, 30)
pwm(13, 100)


s1 = ShotType(50, 50, 0, 0, "Forward", "Center, Center")
s2 = ShotType(50, 0, 0, 0, "Forward", "Left, Center")
s3 = ShotType(50, 100, 0, 0, "Forward", "Right, Center")
