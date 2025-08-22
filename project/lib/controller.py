from wheels import Wheels
from display import Display
from PiicoDev_Unified import sleep_ms
from colour import Colour
import random
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from servo import Servo
from machine import Pin, PWM
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0]) 
csensor = PiicoDev_VEML6040()
rihwheel = Servo(pwm=PWM(Pin(15)))
lefwheel = Servo(pwm=PWM(Pin(16)))
display = create_PiicoDev_SSD1306()

controls = Controller(lefwheel, rihwheel, range_a, range_b, csensor, display, True)

# subsystem for reading all sensors
class ReadingSubsystem():
    def __init__(self, sensora, sensorb, colour, debug):
        self.__debug  = debug
        self.__sensora = sensora
        self.__sensorb = sensorb
        self.__colour = Colour(colour, True)
    def get_rangea(self):
        # get range from front sensor
        return(self.__sensora.distance_mm)
    def get_rangeb(self):
        # get range from right sensor
        return(self.__sensorb.distance_mm)
    def get_colour(self):
        return(self.__colour.readcolour())
# main controller class
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
        # debug statement
        print('running')
        # display debug info on OLED
        self.__display.showtext((self.__reading.get_rangea(), self.__reading.get_rangeb()), self.__reading.get_colour())
        # if it finds green
        if self.__reading.get_colour() == 'green':
            # stops the robot
            self.set_idle_state()
            self.__display.showtext('YIPPIEEEEEE', self.__reading.get_colour())
            sleep_ms(2000)
            # moves forward to not get stuck on green
            self.set_med_state()
            sleep_ms(2000)
        if self.__reading.get_rangea() > 200:
            # fast when far away
            self.set_fast_state()
        elif 120 < self.__reading.get_rangea() < 200:
            # slows down as it gets closer
            self.set_med_state()
        elif 80 < self.__reading.get_rangea() < 120:
            # slow when very close
            self.set_slow_state()
        elif self.__reading.get_rangea() < 80:
            # when within 80mm of a wall in front look for a wall to the right and turn accordingly
            if self.__reading.get_rangeb() < 87:
                self.set_rturn_state()
            else:
                self.set_lturn_state()
        else:
            # stop robot in case of error
            self.set_idle_state()
            self.__display.showtext('error', 'error')

while True:
    controls.update()