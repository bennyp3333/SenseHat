from sense_hat import SenseHat
import time
import random

sense = SenseHat()

r = 0
g = 100
b = 67

sense.clear((r, g, b))
x=0.05
blue = (0, 0, 255)
yellow = (255, 255, 0)
count = 0
while(True):
    
    if x > 0:
        x -= .01
    line = random.randint(0,7)
    for i in range(0,8):
        sense.set_pixel(i, count, [r, g, b])

    count += 1
    if r<255 and g<255 and b<255:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
    else:
        #print("At max values")
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
    time.sleep(0.1)
    if count == 8:
        count = 0
