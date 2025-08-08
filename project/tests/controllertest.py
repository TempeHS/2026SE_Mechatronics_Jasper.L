from controller import Controller
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from servo import Servo
from machine import Pin, PWM

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])

rihwheel = Servo(pwm=PWM(Pin(15)))
lefwheel = Servo(pwm=PWM(Pin(16)))

controls = Controller(lefwheel, rihwheel, True)

while True:
    controls.set_idle_state()