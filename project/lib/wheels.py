from time import sleep
from machine import Pin, PWM
from servo import Servo

servo_pwm = PWM(Pin(16))
my_servo = Servo(pwm=servo_pwm)

class Wheels():
    def __init__(self, lwheel, rwheel, debug=True):
        self.__debug = debug
        self.__lwheel = lwheel
        self.__rwheel = rwheel
    def forward(self):
        self.__lwheel.set_duty(1000)
        self.__rwheel.set_duty(2000)
        if self.__debug:
            print('this wont print but put on OLED eventually')
