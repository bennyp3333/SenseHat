from sense_hat import SenseHat
import time
import random
sense = SenseHat()

I = [0, 128, 248]
L = [139, 68, 16]

class log:
  def __init__(self, logy):
    self.logy = logy
    self.logx = random.randrange(-30,0)
  def moveLog(self):
    rand = random.randrange(1,10)
    if self.logx > -1 and self.logx < 8:
      if rand<6:
        sense.set_pixel(self.logx, self.logy, L)
      else:
        sense.set_pixel(self.logx, self.logy, I)
    self.logx += 1
    if self.logx > 8:
      self.logx = random.randrange(-30,0)
def logs():
  log1 = log(2)
  log2 = log(3)
  log3 = log(4)
  log4 = log(5)
  while True:
    log1.moveLog()
    log2.moveLog()
    log3.moveLog()
    log4.moveLog()
    time.sleep(0.5)
logs()
