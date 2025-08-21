from colour import Colour
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
from PiicoDev_SSD1306 import *

csensor = PiicoDev_VEML6040()
colours = Colour(csensor, True)
display = create_PiicoDev_SSD1306()

while True:
    # shows the colour sensor data on the OLED screen
    display.fill(0)
    display.text(str(colours.readcolour()), 30, 20, 1)
    display.show()
    sleep_ms(100)