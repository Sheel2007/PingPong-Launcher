from gpiozero import AngularServo
from time import sleep

servo1 = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(2, min_pulse_width=0.0006, max_pulse_width=0.0023)

while True:
    servo1.angle = 90
    servo2.angle = 90
    sleep(2)
    servo1.angle = 0
    servo2.angle = 0
    sleep(2)
    servo1.angle = -90
    servo2.angle = -90
    sleep(2)
