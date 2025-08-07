from time import sleep
from machine import Pin, PWM
from wheels import Wheels
from servo import Servo

rihwheel = Servo(pwm=PWM(Pin(16)))
lefwheel = Servo(pwm=PWM(Pin(15)))

rihwheel.set_duty(1700)
sleep(2)
rihwheel.set_duty(1500)
lefwheel.set_duty(1300)
sleep(2)
lefwheel.set_duty(1500)
sleep(5)
rihwheel.set_duty(1850)
sleep(2)
rihwheel.set_duty(1500)
lefwheel.set_duty(1150)
sleep(2)
lefwheel.set_duty(1500)
sleep(5)
rihwheel.set_duty(2000)
sleep(2)
rihwheel.set_duty(1500)
lefwheel.set_duty(1000)
sleep(2)
lefwheel.set_duty(1500)
sleep(5)

'''
wheels = Wheels(lefwheel, rihwheel, True)

while True:
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
'''