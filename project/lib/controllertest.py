import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from servo import Servo
from controller import Controller
from machine import Pin, PWM
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1]) 
csensor = PiicoDev_VEML6040()
rihwheel = Servo(pwm=PWM(Pin(15)))
lefwheel = Servo(pwm=PWM(Pin(16)))
display = create_PiicoDev_SSD1306()

controls = Controller(lefwheel, rihwheel, range_a, range_b, csensor, display, True)

while True:
    controls.update()