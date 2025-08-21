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
    controls.set_idle_state()
    print('Pass if: wheels not moving')
    sleep_ms(5000)
    controls.set_fast_state()
    print('Pass if: wheels moving fast')
    sleep_ms(5000)
    controls.set_med_state()
    print('Pass if: wheels moving at a decent speed')
    sleep_ms(5000)
    controls.set_slow_state()
    print('Pass if: wheels moving slowly')
    sleep_ms(5000)
    controls.set_rturn_state()
    print('Pass if: robot turns right and pauses for about 0.2 seconds')
    sleep_ms(5000)
    controls.set_lturn_state()
    print('Pass if: robot turns left and pauses for about 0.2 seconds')
    sleep_ms(5000)