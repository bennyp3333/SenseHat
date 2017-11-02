from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause

sense = SenseHat()




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
E = [50, 50, 50]  # Grey
W = [255, 255, 255]  # White

menu = [
W, W, W, W, W, W, W, W,
W, W, W, I, I, W, W, W,
W, W, W, I, I, W, W, W,
W, W, W, I, I, W, W, W,
W, W, W, I, I, W, W, W,
W, W, D, D, D, D, W, W,
W, W, W, D, D, W, W, W,
W, W, W, W, W, W, W, W
]
game1 = [
I, I, I, I, I, I, O, Y,
I, I, I, I, I, I, I, O,
K, I, I, I, I, I, I, I,
I, K, I, I, I, I, I, I,
I, I, K, I, R, I, I, I,
I, R, R, R, R, R, I, I,
I, K, R, R, R, K, L, L,
G, G, G, G, G, G, G, G
]
game2 = [
R, O, O, O, O, O, O, R,
O, O, C, P, C, O, O, O,
O, C, G, L, G, C, O, O,
O, P, L, B, L, P, O, O,
O, C, G, L, G, C, O, O,
O, O, C, P, C, O, O, O,
O, O, O, O, O, O, O, O,
R, O, O, O, O, O, O, R
]

sense.set_pixels(menu)
state = 'menu'
right = False
while(True):
    if(state == 'menu'):
        sense.set_pixels(menu)
    elif(state == 'game1'):
        sense.set_pixels(game1)
    elif(state == 'game2'):
        sense.set_pixels(game2)
        
    for event in sense.stick.get_events():
        if(event.action == 'pressed' and event.direction == 'down'):
            if(state == 'menu'):
                state = 'game1'
        if(event.action == 'pressed' and event.direction == 'up'):
            if(state == 'game1'):
                state = 'menu'
            elif(state == 'game2'):
                state = 'menu'
        if(event.action == 'pressed' and event.direction == 'right'):
            if(state == 'game1'):
                state = 'game2'
            elif(state == 'game2'):
                state = 'game1'
        if(event.action == 'pressed' and event.direction == 'left'):
            if(state == 'game1'):
                state = 'game2'
            elif(state == 'game2'):
                state = 'game1'
    ##pause()


