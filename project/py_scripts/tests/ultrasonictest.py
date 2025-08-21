from PiicoDev_Unified import sleep_ms
from ultrasonic import Ultrasonic
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])

sonics = Ultrasonic(range_a, range_b, True)

while True:
    # checking if the data being returned from the class is correct
    print(sonics.reada)
    print(range_a.distance_mm)
    sleep_ms(100)