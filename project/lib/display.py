from PiicoDev_Unified import sleep_ms
from PiicoDev_SSD1306 import *

class Display():
    def __init__(self, display, debug):
        self.__debug = debug
        self.__display = display
    def showtext(self, text1, text2):
        self.__display.fill(0)
        self.__display.text(str(text1), 20, 25, 1)
        self.__display.text(str(text2), 20, 15, 1)
        self.__display.show()