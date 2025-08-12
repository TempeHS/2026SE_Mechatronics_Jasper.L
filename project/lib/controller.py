import time
from wheels import Wheels
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from servo import Servo
from machine import Pin, PWM

class Controller():
    def __init__(self, lwheel, rwheel, debug):
        self.__debug = debug
        self.__wheels = Wheels(lwheel, rwheel, True)
    def set_idle_state(self):
        self.__wheels.medforward()
    def set_rturn_state(self):
        self.__wheels.rightturn()
        