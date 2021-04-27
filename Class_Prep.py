#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT)    # direction control t.1
#GPIO.setup(18, GPIO.OUT)    # direction control t.2
#GPIO.setup(29, GPIO.OUT)    # direction control b.1
#GPIO.setup(31, GPIO.OUT)    # direction control b.2


class ShotType:
    def __init__(self, motor1, motor2, servo1, servo2, direction, description):
        self.motor1 = motor1
        self.motor2 = motor2
        self.servo1 = servo1
        self.servo2 = servo2
        self.direction = direction
        self.description = description

class PWM:
    def __init__(self, ):



s1 = ShotType(50, 50, 0, 0, "Forward", "Center, Center")
s2 = ShotType(50, 0, 0, 0, "Forward", "Left, Center")
s3 = ShotType(50, 100, 0, 0, "Forward", "Right, Center")

s1.motor1
s1.name

