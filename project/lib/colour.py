from time import sleep

class Colour():
    def __init__(self, sensor, debug):
        self.__debug = debug
        self.__sensor = sensor
    def readcolour(self):
        if self.__debug:
            print('reading')
        data = self.__sensor.readHSV() # Read the sensor
        hue = data['hue']
        # we only need if green or not so that is what is returned
        if 75 < hue < 90:
            return 'green'
        else:
            return 'not green'