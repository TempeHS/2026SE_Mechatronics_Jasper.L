from time import sleep
from machine import Pin, PWM
from wheels import Wheels
from servo import Servo

rihwheel = Servo(pwm=PWM(Pin(16)))
lefwheel = Servo(pwm=PWM(Pin(15)))

wheels = Wheels(lefwheel, rihwheel, True)

while True:
    wheels.forward()