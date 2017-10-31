from sense_hat import SenseHat
import time
sense = SenseHat()
# max rgb values are [248,252,248]
  
def frogger():
  x, lastx, y, lasty = 0, 0, 7, 7
  colors = [[0,128,0], [51,170,255], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
  frog = 0
  background = 1
  for i in range(0,8):
    for j in range(0,8):
      sense.set_pixel(i,j, colors[background])
  while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colors[frog])
        if event.action == 'pressed' and event.direction == 'up':
          lasty = y
          y -= 1
          sense.set_pixel(x, lasty, colors[background])
        if event.action == 'pressed' and event.direction == 'down':
          lasty = y
          y += 1
          sense.set_pixel(x, lasty, colors[background])
        if event.action == 'pressed' and event.direction == 'right':
          lastx = x
          x += 1
          sense.set_pixel(lastx, y, colors[background])
        if event.action == 'pressed' and event.direction == 'left':
          lastx = x
          x -= 1
          sense.set_pixel(lastx, y, colors[background])
frogger()
