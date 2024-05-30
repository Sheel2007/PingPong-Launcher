from gpiozero import AngularServo
from time import sleep

servo_x = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo_y = AngularServo(2, min_pulse_width=0.0006, max_pulse_width=0.0023)
trigger = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

def shoot(servo_x_angle, servo_y_angle):
    # sleep(1)

    servo_x.angle = servo_x_angle
    servo_y.angle = servo_y_angle

    sleep(1)

    trigger.angle = 60

    sleep(1)

    trigger.angle = 0

def reset():
    sleep(1)

    servo_x.angle = 0
    servo_y.angle = 0

    sleep(1)

    trigger.angle = 0

reset()