import time
from wheels import Wheels

class Controller():
    def __init__(self, lwheel, rwheel, debug):
        self.__debug = debug
        self.__wheels = Wheels(lwheel, rwheel, True)
    def set_idle_state(self):
        self.__wheels.medforward()