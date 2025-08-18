from wheels import Wheels
from display import Display
from PiicoDev_Unified import sleep_ms
from colour import Colour
import random

# subsystem for reading all sensors
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
        return(self.__colour.readcolour())

class Controller():
    def __init__(self, lwheel, rwheel, sensora, sensorb, colour, display, debug):
        # initialise sensors and such into classes
        self.__debug = debug
        self.__wheels = Wheels(lwheel, rwheel, True)
        self.__reading = ReadingSubsystem(sensora, sensorb, colour, True)
        self.__display = Display(display, True)
    def set_idle_state(self):
        self.__wheels.stop()
    def set_fast_state(self):
        self.__wheels.fastforward()
    def set_med_state(self):
        self.__wheels.medforward()
    def set_slow_state(self):
        self.__wheels.slowforward()
    def set_rturn_state(self):
        self.__wheels.rightturn()
        sleep_ms(random.randint(770, 820))
        self.__wheels.stop()
        sleep_ms(200)
    def set_lturn_state(self):
        self.__wheels.leftturn()
        sleep_ms(random.randint(900, 950))
        self.__wheels.stop()
        sleep_ms(200)
    # main update loop aka state machine
    def update(self):
        print('running')
        self.__display.showtext((self.__reading.get_rangea(), self.__reading.get_rangeb()), self.__reading.get_colour())
        if self.__reading.get_colour() == 'green':
            self.set_idle_state()
            self.__display.showtext('YIPPIEEEEEE', self.__reading.get_colour())
            sleep_ms(2000)
            self.set_med_state()
            sleep_ms(2000)
        if self.__reading.get_rangea() > 200:
            self.set_fast_state()
        elif 120 < self.__reading.get_rangea() < 200:
            self.set_med_state()
        elif 80 < self.__reading.get_rangea() < 120:
            self.set_slow_state()
        elif self.__reading.get_rangea() < 80:
            if self.__reading.get_rangeb() < 87:
                self.set_lturn_state()
            else:
                self.set_rturn_state()
        else:
            self.set_idle_state()