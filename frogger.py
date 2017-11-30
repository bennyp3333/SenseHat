from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# max rgb values are [248,252,248]
R = [255, 0, 0]  # Red
O = [255, 128, 0]  # orange
Y = [255, 255, 0]  # Yellow
L = [139, 68, 16]  # Log

G = [0, 255, 0]  # Green
S = [0, 100, 0]  # Dark Green
C = [0, 255, 255]  # Cyan
I = [0, 128, 248]  # Light Blue, Indigo?

B = [0, 0, 255]  # Blue
P = [120, 0, 248]  # Purple
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
class log:
  def __init__(self, logy):
    self.logy = logy
    self.logx = random.randrange(-30,0)
  def moveLog(self):
    rand = random.randrange(1,10)
    if self.logx > -1 and self.logx < 8:
      if rand<6 and sense.get_pixel(self.logx, self.logy) != P:
        sense.set_pixel(self.logx, self.logy, L)
      else:
        sense.set_pixel(self.logx, self.logy, I)
        if sense.get_pixel(self.logx, self.logy) == P:
          frogger()
    self.logx += 1
    if self.logx > 8:
      self.logx = random.randrange(-30,0)

def xy(x, y):
  return((y*8)+x)

def frogger():
  log1 = log(2)
  log2 = log(3)
  log3 = log(4)
  log4 = log(5)
  
  x, lastx, y, lasty = 0, 0, 7, 7

  for i in range(0,8):
    for j in range(0,8):
      sense.set_pixels(bg)
  sense.set_pixel(0, 7, P)
  counter = 0
  wasLog = 0
  while True:
    if counter >= 30:
      log1.moveLog()
      log2.moveLog()
      log3.moveLog()
      log4.moveLog()
      counter = 0
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, P)
        if event.action == 'pressed' and event.direction == 'up' and y>0:
          if sense.get_pixel(x, y-1) == I:
            frogger()
          if y-1==0:
            exit()
          lasty = y
          y -= 1
          sense.set_pixel(x, lasty, bg[xy(x, lasty)])
        if event.action == 'pressed' and event.direction == 'down' and y<7:
          if sense.get_pixel(x, y+1) == I:
            frogger()
          lasty = y
          y += 1
          sense.set_pixel(x, lasty, bg[xy(x, lasty)])
        if event.action == 'pressed' and event.direction == 'right' and x<7:
          if sense.get_pixel(x+1, y) == I:
            frogger()
          lastx = x
          x += 1
          sense.set_pixel(lastx, y, bg[xy(lastx, y)])
        if event.action == 'pressed' and event.direction == 'left' and x>0:
          if sense.get_pixel(x-1, y) == I:
            frogger()
          lastx = x
          x -= 1
          sense.set_pixel(lastx, y, bg[xy(lastx, y)])
    time.sleep(0.01)
    counter += 1
    print(sense.get_pixel(0,7))
frogger()
