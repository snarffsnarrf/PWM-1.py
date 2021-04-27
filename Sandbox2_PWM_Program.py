
# A test for PWM and experimenting with frequency & duty cycle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

p_freq = 100        # Master PWM Frequency
tfreq = p_freq      # top Frequency in Hz
bfreq = p_freq      # bottom Frequency in Hz
wstrt = 3           # time between wheels start
wrmp = 2            # time between wheels ramp up
err = "Not a valid entry"

# Control Module
int_spd = 25
strt_spd = 35
spd = 5
load_tm = .25

top = GPIO.PWM(11, tfreq)
bot = GPIO.PWM(13, bfreq)


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
        GPIO.output(29, True)
        GPIO.output(31, False)  # Can change when you get a real second motor.
        bot.start(int_spd)
        time.sleep(wstrt)
        top.start(int_spd)
        time.sleep(wstrt)
        top.ChangeDutyCycle(strt_spd)
        time.sleep(wrmp)
        bot.ChangeDutyCycle(strt_spd)
        time.sleep(wrmp)
        top.ChangeDutyCycle(100)
        bot.ChangeDutyCycle(100)
        time.sleep(wrmp)
        top.ChangeDutyCycle(40)
        bot.ChangeDutyCycle(40)
        time.sleep(wrmp)
        top.ChangeDutyCycle(100)
        bot.ChangeDutyCycle(100)
        time.sleep(wrmp)
        top.ChangeDutyCycle(40)
        bot.ChangeDutyCycle(40)
        time.sleep(wrmp)
        top.ChangeDutyCycle(0)
        bot.ChangeDutyCycle(100)
        time.sleep(wrmp)
        top.ChangeDutyCycle(100)
        bot.ChangeDutyCycle(0)
        time.sleep(wrmp)
        top.ChangeDutyCycle(100)
        bot.ChangeDutyCycle(100)
        time.sleep(wrmp)
        top.ChangeDutyCycle(40)
        bot.ChangeDutyCycle(40)
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
                    top.ChangeDutyCycle(s)
                    bot.ChangeDutyCycle(s)
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
                                    top.stop()
                                    bot.stop()
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
        top.stop()
        bot.stop()
        break
GPIO.cleanup()
