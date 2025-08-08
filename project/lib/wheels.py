from time import sleep
from machine import Pin, PWM
from servo import Servo

class Wheels():
    def __init__(self, lwheel, rwheel, debug=True):
        self.__debug = debug
        self.__lwheel = lwheel
        self.__rwheel = rwheel
    def slowforward(self):
        self.__lwheel.set_duty(1700)
        self.__rwheel.set_duty(1300)
    def medforward(self):
        self.__lwheel.set_duty(1850)
        self.__rwheel.set_duty(1150)
    def fastforward(self):
        self.__lwheel.set_duty(2000)
        self.__rwheel.set_duty(1000)
    def slowback(self):
        self.__lwheel.set_duty(1300)
        self.__rwheel.set_duty(1700)
    def medback(self):
        self.__lwheel.set_duty(1150)
        self.__rwheel.set_duty(1850)
    def fastback(self):
        self.__lwheel.set_duty(1000)
        self.__rwheel.set_duty(2000)
    def rightturn(self):
        self.__lwheel.set_duty(1200)
        self.__rwheel.set_duty(1200)
    def leftturn(self):
        self.__lwheel.set_duty(1800)
        self.__rwheel.set_duty(1800)
