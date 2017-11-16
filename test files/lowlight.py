import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255, 255, 255)
while(True):
    sense.low_light = True
    time.sleep(.5)
    sense.low_light = False
    time.sleep(.5)