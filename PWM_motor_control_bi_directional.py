
# A test for PWM and experimenting with frequency & duty cycle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control?
GPIO.setup(18, GPIO.OUT)    # direction control?

freq = 100
tfreq = freq     # top Frequency in Hz
bfreq = freq     # bottom Frequency in Hz
wstrt = 3       # time between wheels start
wstrt2 = 2      # ''                   '' 2
err = ("Not a valid entry")

int_spd = 25
strt_spd = 35
spd = 5
load_tm = .25

t = GPIO.PWM(11, tfreq)
b = GPIO.PWM(13, bfreq)


command = ""
start = ""

while True:
    command = input(">>> ").lower()
    if command == "start":          # Startup - bottom motor>top>top goes to idle> bottom idle
        i = 1
        while i <= 5:               # Loading screen
            i = i + 1
            print("-" * i)
            time.sleep(load_tm)
        GPIO.output(16, True)
        GPIO.output(18, False)
        b.start(int_spd)
        time.sleep(wstrt)
        t.start(int_spd)
        time.sleep(wstrt)
        t.ChangeDutyCycle(strt_spd)
        time.sleep(wstrt2)
        b.ChangeDutyCycle(strt_spd)
        # Removing time.sleep(wstrt2) on this line for faster boot?
        i = 6
        while i <= 10:               # Loading screen
            i = i + 1
            print("-" * i)
            time.sleep(load_tm)
        while True:
            try:
                s = float(input("What speed do you want? 1-100 : "))
                if 100 < s or s < 0:
                    print(err)
                if 0 <= s <= 100:
                    t.ChangeDutyCycle(s)
                    b.ChangeDutyCycle(s)
                    print("Changing speed")
                if s == "quit":
                    GPIO.cleanup()
                    time.sleep(1)
                    quit()
            except ValueError:
                print(err)
            else:
                while True:
                    cont = input("Do you want to change the speed? Y/N : ").lower()
                    if cont == "y":
                        break
                    if cont == "n":
                        code_1 = input("Do you want to quit? : ").lower()
                        if code_1 == "y":
                            while True:
                                code_2 = input("Are you sure? Y/N : ").lower()
                                if code_2 == "y":
                                    t.stop()
                                    b.stop()
                                    GPIO.cleanup()
                                    time.sleep(1)
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
