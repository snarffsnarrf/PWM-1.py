# A test for PWM and experimenting with frequency & duty cycle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
tfreq = 500  # top Frequency
bfreq = 500  # bottom Frequency
wstrt = 5   # time between wheel startup
ofst = 3    # offset for wheel control

int_spd = 10
strt_spd = 50
spd = 5

t = GPIO.PWM(11, tfreq)
b = GPIO.PWM(13, bfreq)

command = ""

while True:
    command = input(">>> ").lower()
    if command == "start":
        b.start(int_spd)
        time.sleep(wstrt)
        t.start(int_spd)
        time.sleep(10)
        t.ChangeDutyCycle(strt_spd)
        time.sleep(ofst)
        b.ChangeDutyCycle(strt_spd)
        time.sleep(5)
        i = 1
        while i <= 5:
            i = i + 1
            print("-" * i)
            time.sleep(.5)
        s = int(input("what speed do you want? 1-100 : "))
        if 0 <= s <= 100:
            t.ChangeDutyCycle(s)
            b.ChangeDutyCycle(s)
        else:
            print("not a valid entry. ")
    elif command == "quit":
        t.stop(0)
        b.stop(0)
        break
GPIO.cleanup()
