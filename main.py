# A test for PWM and experimenting with frequency & duty cycle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
tfreq = .1  # top Frequency
bfreq = .1  # bottom Frequency
t = GPIO.PWM(11, tfreq)
b = GPIO.PWM(13, bfreq)

command = ""

while True:
    command = input(">>> ").lower()
    if command == "start":
        b.start(10)
        time.sleep(1)
        t.start(10)
        time.sleep(2)
        t.ChangeDutyCycle(50)
        b.ChangeDutyCycle(50)
    elif command == "quit":
        t.start(0)
        b.start(0)
        break
