import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control?
GPIO.setup(18, GPIO.OUT)



GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(11, True)
GPIO.output(13, True)


s = input("stop")
if s == "stop":
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.cleanup()

