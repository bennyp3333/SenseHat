from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import time
import os

R = [255, 0, 0]  # Red
O = [255, 128, 0]  # orange
Y = [255, 255, 0]  # Yellow
L = [128, 255, 0]  # Lime?

G = [0, 255, 0]  # Green
S = [0, 255, 128]  # Spring Green?
C = [0, 255, 255]  # Cyan
I = [0, 128, 255]  # Light Blue, Indigo?

B = [0, 0, 255]  # Blue
P = [127, 0, 255]  # Purple
H = [255, 0, 255]  # Hot Pink
D = [255, 0, 127]  # Dark Red/Pink

K = [0, 0, 0]  # Black
E = [100, 100, 100]  # Grey
W = [255, 255, 255]  # White

screen = [
K, K, K, K, K, K, K, K,
K, R, K, B, K, K, K, K,
K, K, K, K, K, K, K, K,
K, P, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, G, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
L, L, I, I, I, I, I, C, 
]
files = [
K, K, K, K, K, K, K, K,
K, I, I, I, I, I, R, K,
K, E, E, E, E, E, E, K,
K, E, Y, E, Y, E, E, K,
K, E, E, E, E, E, E, K,
K, E, E, E, E, E, E, K,
K, K, K, K, K, K, K, K,
L, L, I, I, I, I, I, C, 
]
menu = [
K, K, K, K, K, K, K, K,
K, R, K, B, K, K, K, K,
K, K, K, K, K, K, K, K,
I, I, K, K, K, K, K, K,
E, C, K, K, K, K, K, K,
E, C, K, K, K, K, K, K,
E, C, K, K, K, K, K, K,
L, L, I, I, I, I, I, C, 
]
profile = [
W, W, W, W, W, W, W, W,
W, W, W, B, B, W, W, W,
W, W, B, B, B, B, W, W,
W, W, B, B, B, B, W, W,
W, W, W, B, B, W, W, W,
W, W, W, B, B, W, W, W,
W, B, B, B, B, B, B, W,
W, B, B, B, B, B, B, W
]

x = 3
y = 3
sense = SenseHat()

state = 'screen'

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))
def refresh():
    sense.clear()
    if(state == 'screen'):
        sense.set_pixels(screen)
    elif(state == 'menu'):
        sense.set_pixels(menu)
    elif(state == 'files'):
        sense.set_pixels(files)
    elif(state == 'profile'):
        sense.set_pixels(profile)
    sense.set_pixel(x, y, 255, 255, 255)
    print("X:{0}    Y:{1}".format(x, y))
refresh()
while(True):  
    for event in sense.stick.get_events():
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'down'):
            y = clamp(y + 1)
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'up'):
            y = clamp(y - 1)
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'right'):
            x = clamp(x + 1)
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'left'):
            x = clamp(x - 1)
        if(event.action == 'pressed' and event.direction == 'middle'):
            if(x < 2 and y > 6):
                state = 'menu'
            elif(x == 1 and y == 1 and state == 'screen'):#game1
                os.system("python game1.py")
            elif(x == 1 and y == 3 and state == 'screen'):#game2
                os.system("python game2.py")
            elif(x == 1 and y == 5 and state == 'screen'):#game3
                os.system("python game3.py")
            elif(x == 3 and y == 1 and state == 'screen'):#game4
                os.system("python game4.py")
            elif(x == 1 and y == 4 and state == 'menu'):#files
                state = 'files'
            elif(x == 0 and y == 3 and state == 'menu'):#profile
                state = 'profile'
            elif(x < 2 and y > 3 and state == 'menu'):#menu click
                state = 'menu'
            else:
                state = 'screen'
        refresh()
        print("Actoin:{0}    Direction:{1}".format(event.action, event.direction))
        #pause()

