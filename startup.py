from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import time
import os
import pygame

pygame.init()
pygame.mixer.music.load('sounds/Microsoft_Windows_XP_Startup_Sound[Mp3Converter.net].mp3')
pygame.mixer.music.play()

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

backdrop1 = [
K, K, K, K, K, K, K, K,
K, K, K, K, O, L, K, K,
K, K, K, K, B, Y, K, K,
K, K, W, W, W, W, K, K,
K, K, K, K, K, K, K, K,
K, K, B, E, E, E, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K, 
]
backdrop2 = [
K, K, K, K, K, K, K, K,
K, K, K, K, O, L, K, K,
K, K, K, K, B, Y, K, K,
K, K, W, W, W, W, K, K,
K, K, K, K, K, K, K, K,
K, K, E, B, E, E, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K, 
]
backdrop3 = [
K, K, K, K, K, K, K, K,
K, K, K, K, O, L, K, K,
K, K, K, K, B, Y, K, K,
K, K, W, W, W, W, K, K,
K, K, K, K, K, K, K, K,
K, K, E, E, B, E, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K, 
]
backdrop4 = [
K, K, K, K, K, K, K, K,
K, K, K, K, O, L, K, K,
K, K, K, K, B, Y, K, K,
K, K, W, W, W, W, K, K,
K, K, K, K, K, K, K, K,
K, K, E, E, E, B, K, K,
K, K, K, K, K, K, K, K,
K, K, K, K, K, K, K, K, 
]
sense = SenseHat()
n = 0
pygame.mixer.music.play()
while(n < 10):
    sense.set_pixels(backdrop1)
    time.sleep(0.1)
    sense.set_pixels(backdrop2)
    time.sleep(0.1)
    sense.set_pixels(backdrop3)
    time.sleep(0.1)
    sense.set_pixels(backdrop4)
    time.sleep(0.1)
    n = n + 1
#run menu  
os.system("python menu2.py")
