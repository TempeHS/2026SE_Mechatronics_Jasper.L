from display import Display
from PiicoDev_Unified import sleep_ms
from PiicoDev_SSD1306 import *

display = create_PiicoDev_SSD1306()
oled = Display(display, True)

while True:
    oled.showtext('testing', 'test')