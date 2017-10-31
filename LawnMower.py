from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]
class mowing:
  
  def __init__(self, sense):
    self.sense = sense
    self.count = 5 #temporary
    self.moveThresh = 30
    self.grassColor = [0,252,0]
    self.rockColor = [175,155,140]
    
  def lawnMower(self):
    
    temp = sense.get_temperature()
    self.createField()
    loX, lastX, loY, lastY = 0, 0, 7, 7
    points = 0
    sense.set_pixel(loX, loY, [248, 0, 32])
    
    while(True):
      orient = sense.get_orientation()
      x = orient["pitch"]
      y = orient["roll"]
      
      if (y > self.moveThresh and y < 180 and loY < 7):
        if(sense.get_pixel(loX, loY+1)==self.grassColor):
          points+=1
        loY = lastY+1
      elif(y < 360 - self.moveThresh and y > 180 and loY > 0):
        if(sense.get_pixel(loX, loY-1)==self.grassColor):
          points+=1
        loY = lastY-1
      if (x > self.moveThresh and x < 180 and loX > 0):
        if(sense.get_pixel(loX-1, loY)==self.grassColor):
          points+=1
        loX = lastX-1
      elif (x < 360 - self.moveThresh and x > 180 and loX < 7):
        if(sense.get_pixel(loX+1, loY)==self.grassColor):
          points+=1
        loX = lastX+1
        
      sense.set_pixel(lastX, lastY, [2, 252, 119])
      lastX = loX
      lastY = loY
      sense.set_pixel(loX, loY, [248, 2, 36])
      if(points == 64):
        print("You Won!")
      print(points)
      #print(x, y, temp)
      
      time.sleep(1)
    
  
  def createField(self):
    for i in range(0,8):
      for j in range(0,8):
        sense.set_pixel(i,j, self.grassColor)
    for i in range(self.count):
      sense.set_pixel(random.randint(0,7), random.randint(0,7), self.rockColor)
   

sense = SenseHat()
sense.clear()
mowing = mowing(sense)
mowing.lawnMower()
