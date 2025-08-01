import time
from machine import Pin, PWM
from servo import Servo

# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

class Wheels(Pin):
    def __init__(self, pin, debug):
        self.__debug = debug
        self.__pin = pin
        self.moving = False
        