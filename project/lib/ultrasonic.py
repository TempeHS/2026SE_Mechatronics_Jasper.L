from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class Ultrasonic():
    def __init__(self, sensora, sensorb, debug):
        self.__debug = debug
        self.__sensora = sensora
        self.__sensorb = sensorb
    def reada(self):
        thing = self.__sensora.distance_mm
        return(thing)