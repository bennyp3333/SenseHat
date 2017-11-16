from sense_hat import SenseHat
import time

from sense_hat import SenseHat

sense = SenseHat()

n = 1

numPics = 1

while(True):
    sense.clear()
    sense.load_image("pictures/picture{0}.png".format(n))
    for event in sense.stick.get_events():
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'right'):
            n = n + 1
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'left'):
            n = n - 1
    if(n >= numPics):
        n = 1