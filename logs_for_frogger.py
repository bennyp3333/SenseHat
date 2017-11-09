from sense_hat import SenseHat
import time
sense = SenseHat()
R = [255, 0, 0]  # Red
O = [255, 128, 0]  # orange
Y = [255, 255, 0]  # Yellow
L = [128, 255, 0]  # Lime?

G = [0, 255, 0]  # Green
S = [0, 252, 128]  # Spring Green?
C = [0, 255, 255]  # Cyan
I = [0, 128, 248]  # Light Blue, Indigo?

B = [0, 0, 255]  # Blue
P = [127, 0, 255]  # Purple
H = [255, 0, 255]  # Hot Pink
D = [255, 0, 127]  # Dark Red/Pink

K = [0, 0, 0]  # Black
E = [50, 50, 50]  # Grey
W = [255, 255, 255]  # White
bg = [
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
I, I, I, I, I, I, I, I,
I, I, I, I, I, I, I, I,
I, I, I, I, I, I, I, I,
I, I, I, I, I, I, I, I,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G
]
while True:
  for event in sense.stick.get_events():
      sense.set_pixel(x, y, S)
      if event.action == 'pressed' and event.direction == 'up' and y>0 and sense.get_pixel(x, y-1) != I:
        lasty = y
        y -= 1
        sense.set_pixel(x, lasty, bg[xy(x, lasty)])
      if event.action == 'pressed' and event.direction == 'down' and y<7 and sense.get_pixel(x, y+1) != I:
        lasty = y
        y += 1
        sense.set_pixel(x, lasty, bg[xy(x, lasty)])
      if event.action == 'pressed' and event.direction == 'right' and x<7 and sense.get_pixel(x+1, y) != I:
        lastx = x
        x += 1
        sense.set_pixel(lastx, y, bg[xy(lastx, y)])
      if event.action == 'pressed' and event.direction == 'left' and x>0 and sense.get_pixel(x-1, y) != I:
        lastx = x
        x -= 1
        sense.set_pixel(lastx, y, bg[xy(lastx, y)])
      print(sense.get_pixel(0,7))
