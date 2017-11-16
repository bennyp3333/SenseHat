from sense_hat import SenseHat
import time

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
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K, 
]

numbers = [
0,  1,  2,  3,  4,  5,  6,  7,
8,  9,  10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23,
24, 25, 26, 27, 28, 29, 30, 31,
32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47,
48, 49, 50, 51, 52, 53, 54, 55,
56, 57, 58, 59, 60, 61, 62, 63,
]

sense = SenseHat()
height = 8 ## can be 0, 8, 16
space = 4

def setbgcolor(pixelarray, color):
    n = 0
    while(n < 64):
        pixelarray[n] = color
        n = n +1

def zero(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[8+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[24+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def nine(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[8+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[34+k] = color
    
def eight(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[8+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[24+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def seven(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[2+k] = color
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[26+k] = color
    pixelarray[34+k] = color

def six(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[8+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[24+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def five(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[8+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def four(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[2+k] = color
    pixelarray[10+k] = color
    pixelarray[8+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[34+k] = color
    

def three(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[26+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def two(position, pixelarray, color):
    if (position == 2):
        k = height + space
    else:
        k = height
    pixelarray[0+k] = color
    pixelarray[1+k] = color
    pixelarray[2+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[17+k] = color
    pixelarray[16+k] = color
    pixelarray[24+k] = color
    pixelarray[32+k] = color
    pixelarray[33+k] = color
    pixelarray[34+k] = color

def one(position, pixelarray, color):
    if (position == 2):
        kk = height + space
    else:
        k = height
    pixelarray[2+k] = color
    pixelarray[10+k] = color
    pixelarray[18+k] = color
    pixelarray[26+k] = color
    pixelarray[34+k] = color
    
def displaytemp(first, second, color, backgroundcolor):
    n = 1
    setbgcolor(screen, backgroundcolor)
    while(n < 3):
        if(n == 1):
            time = first
        elif(n == 2):
            time = second
            
        if time == 0:
           zero(n, screen, color)
        elif time == 1:
           one(n, screen, color)
        elif time == 2:
           two(n, screen, color)
        elif time == 3:
           three(n, screen, color)
        elif time == 4:
           four(n, screen, color)
        elif time == 5:
           five(n, screen, color)
        elif time == 6:
           six(n, screen, color)
        elif time == 7:
           seven(n, screen, color)
        elif time == 8:
           eight(n, screen, color)
        elif time == 9:
           nine(n, screen, color)
        n = n + 1
    sense.set_pixels(screen)
    

sun = [
K, K, K, K, K, K, K, K,  
K, K, O, O, O, O, K, K,
K, O, Y, Y, Y, Y, O, K,
K, O, Y, Y, Y, Y, O, K,
K, O, Y, Y, Y, Y, O, K,
K, O, Y, Y, Y, Y, O, K,
K, K, O, O, O, O, K, K,
K, K, K, K, K, K, K, K
]
cloud = [
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, O, O, K, K,
K, K, K, O, Y, Y, O, K,
K, K, E, W, W, Y, O, K,
K, E, W, W, W, W, K, K,
K, W, W, W, W, W, W, K,
K, K, K, K, K, K, K, K, 
]
rain = [
K, K, K, K, K, K, K, K,
K, K, E, W, W, W, K, K,
K, E, W, W, W, W, W, K,
K, K, K, K, K, K, K, K,
K, K, K, K, I, K, K, K,
K, K, I, K, K, K, K, K,
K, K, K, K, K, I, K, K,
K, K, K, K, K, K, K, K, 
]
snow = [
K, K, K, W, K, K, K, K,
K, K, W, W, W, K, K, K,
K, W, K, W, K, W, K, K,
W, W, W, W, W, W, W, K,
K, W, K, W, K, W, K, K,
K, K, W, W, W, K, K, K,
K, K, K, W, K, K, K, K,
K, K, K, K, K, K, K, K, 
]
    
def weatherpicture(temperature):
    if(temperature > 90):
        sense.set_pixels(sun)
    elif(temperature > 60):
        sense.set_pixels(cloud)
    elif(temperature > 30):
        sense.set_pixels(rain)
    elif(temperature > 0):
        sense.set_pixels(snow)
        
        
wait = 3   
        
while(True):
    temp = sense.get_temperature()
    temp = temp * 1.8 + 32
    ##sense.show_message(str(int(temp)), text_colour=R, back_colour=K, scroll_speed=0.1)
    ##eight(1,screen, R)
    ##zero(2,screen, I)
    ##sense.set_pixels(screen)
    displaytemp(int(temp/10), int(temp - (10 * int(temp/10))), W, K)
    print ("real temp: {0}     first digit: {1}    second digit: {2}  ".format(temp,int(temp/10),int(temp - (10 * int(temp/10)))))
    ##displaytemp(6, 9, W, K)
    time.sleep(wait)
    ##sense.set_pixels(rain)
    weatherpicture(temp)
    time.sleep(wait)
    for event in sense.stick.get_events():
        if((event.action == 'pressed' or event.action == 'held') and event.direction == 'middle'):
            print('fuc')
            exit()