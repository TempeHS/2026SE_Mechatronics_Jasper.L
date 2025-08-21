from time import sleep
from machine import Pin, PWM
from wheels import Wheels
from servo import Servo

rihwheel = Servo(pwm=PWM(Pin(15)))
lefwheel = Servo(pwm=PWM(Pin(16)))

wheels = Wheels(lefwheel, rihwheel, True)

while True:
    # checking all of the functions of the wheels
    wheels.slowforward()
    sleep(2)
    wheels.medforward()
    sleep(2)
    wheels.fastforward()
    sleep(2)
    wheels.slowback()
    sleep(2)
    wheels.medback()
    sleep(2)
    wheels.fastback()
    sleep(2)
    wheels.rightturn()
    sleep(2)
    wheels.leftturn()
    sleep(2)