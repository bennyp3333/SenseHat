from sense_hat import SenseHat
import time
import random

sense = SenseHat()

r = 0
g = 100
b = 67

sense.clear((r, g, b))
x=0.07
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255,255,255)
blank = (0,0,0)
count = 0
while(True):
    #sense.show_message(str(round(sense.get_temperature(),2)))
    sense.show_message("EAT MY ASS", text_colour=blue, back_colour=blank, scroll_speed=x)
