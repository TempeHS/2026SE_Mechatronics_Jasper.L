from time import sleep

class Colour():
    def __init__(self, sensor, debug):
        self.__debug = debug
        self.__sensor = sensor
    def readcolour(self):
        if self.__debug:
            print('reading')
        data = self.__sensor.readHSV() # Read the sensor (Colour space: Hue Saturation Value)
        hue = data['hue']
        if 75 < hue < 90:
            return 'green'
        else:
            return 'not green'