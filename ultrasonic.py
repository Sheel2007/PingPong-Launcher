import RPi.GPIO as GPIO
from gpiozero import AngularServo
import time


TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)

servo1 = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(2, min_pulse_width=0.0006, max_pulse_width=0.0023)


while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance = (1.02091 * distance) + 1.06547 # y = mx+b
    # distance=round(distance,2)
    print("distance:",distance,"cm")

    if distance < 50:
        servo1.angle = 90
    else:
        servo1.angle = -90

    time.sleep(2)    