# A test for PWM and experimenting with frequency & duty cycle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
tfreq = 300  # top Frequency
bfreq = 300  # bottom Frequency
wstrt = 2   # time between wheel startup
ofst = 1    # offset for wheel control

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
        time.sleep(5)
        t.ChangeDutyCycle(strt_spd)
        time.sleep(ofst)
        b.ChangeDutyCycle(strt_spd)
        time.sleep(2.5)
        i = 1
        while i <= 5:
            i = i + 1
            print("-" * i)
            time.sleep(.5)
        while True:
            try:
                s = int(input("What speed do you want? 1-100 : "))
                if 0 <= s <= 100:
                    t.ChangeDutyCycle(s)
                    b.ChangeDutyCycle(s)
            except ValueError or (s < 0 or s > 100):
                print("Not a valid entry.")
            else:
                while True:
                    cont = input("Do you want to change the speed? Y/N : ").lower()
                    if cont == "y":
                        break
                    if cont == "n":
                        ex = input("Do you want to quit? : ").lower()
                        if ex == "y":
                            while True:
                                dun = input("Are you sure? Y/N : ").lower()
                                if dun == "y":
                                    quit()
                                else:
                                    break
                        else:
                            break
                    else:
                        print("Not a valid entry. ")
    if command == "quit":
        t.stop()
        b.stop()
        break
GPIO.cleanup()
