import time
from wheels import Wheels
from display import Display
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from machine import Pin, PWM
from colour import Colour
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *


class ReadingSubsystem():
    def __init__(self, sensora, sensorb, colour, debug):
        self.__debug  = debug
        self.__sensora = sensora
        self.__sensorb = sensorb
        self.__colour = Colour(colour, True)
    def get_rangea(self):
        return(self.__sensora.distance_mm)
    def get_rangeb(self):
        return(self.__sensorb.distance_mm)
    def get_colour(self):
        return(
            self.__colour.readcolour()
        )

class Controller():
    def __init__(self, lwheel, rwheel, sensora, sensorb, colour, display, debug):
        self.__debug = debug
        self.__wheels = Wheels(lwheel, rwheel, True)
        self.__reading = ReadingSubsystem(sensora, sensorb, colour, True)
        self.__display = Display(display, True)
    def set_idle_state(self):
        self.__wheels.medforward()
    def set_rturn_state(self):
        self.__wheels.rightturn()
    def set_lturn_state(self):
        self.__wheels.leftturn()

    def update(self):
        print('running')
        self.__display.showtext((self.__reading.get_rangea(), self.__reading.get_rangeb()), self.__reading.get_colour())