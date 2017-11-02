from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]
class mowing:
  
  def __init__(self, sense):
    self.sense = sense
    self.count = 4 #temporary
    self.moveThresh = 30
    self.grassColor = [0,252,0]
    self.rockColor = [168,152,136]
    self.explodeColor = [248,100,0]
    self.xMax, self.yMax = 7, 7 #could set to parameters
    self.availPoints = (self.xMax+1)*(self.yMax+1)
    self.loX, self.loY = 0, self.xMax
    self.lastX, self.lastY = self.loX, self.loY
    
  def lawnMower(self):
    temp = sense.get_temperature()
    self.createField()
    points = 0
    sense.set_pixel(self.loX, self.loY, [248, 2, 36])
    
    while(True):
      orient = sense.get_orientation()
      x = orient["pitch"]
      y = orient["roll"]
      
      if y > self.moveThresh and y < 180 and self.loY < self.xMax:
        if sense.get_pixel(self.loX, self.loY+1)==self.grassColor:
          points+=1
        elif sense.get_pixel(self.loX, self.loY+1)==self.rockColor:
          self.lose()
          break
        self.loY = self.lastY+1
      elif y < 360 - self.moveThresh and y > 180 and self.loY > 0:
        if sense.get_pixel(self.loX, self.loY-1)==self.grassColor:
          points+=1
        elif sense.get_pixel(self.loX, self.loY-1)==self.rockColor:
          self.lose()
          break
        self.loY = self.lastY-1
      if x > self.moveThresh and x < 180 and self.loX > 0:
        if sense.get_pixel(self.loX-1, self.loY)==self.grassColor:
          points+=1
        elif sense.get_pixel(self.loX-1, self.loY)==self.rockColor:
          self.lose()
          break
        self.loX = self.lastX-1
      elif x < 360 - self.moveThresh and x > 180 and self.loX < self.yMax:
        if sense.get_pixel(self.loX+1, self.loY)==self.grassColor:
          points+=1
        elif sense.get_pixel(self.loX+1, self.loY)==self.rockColor:
          self.lose()
          break
        self.loX = self.lastX+1
        
      sense.set_pixel(self.lastX, self.lastY, [2, 252, 119])
      self.lastX, self.lastY = self.loX, self.loY
      sense.set_pixel(self.loX, self.loY, [248, 2, 36])
      
      if points == self.availPoints:
        self.winRound()
      
      time.sleep(1)
      
    sense.show_message("Game has Ended", scroll_speed = 0.0001)
  
  def createField(self):
    for i in range(0,8):
      for j in range(0,8):
        sense.set_pixel(i,j, self.grassColor)
    
    rockList = []
    for i in range(self.count):
      sameRock = True #just to initialize to get into while loop
      while (sameRock == True):
        sameRock = False
        rockLoc = [random.randint(0,self.xMax), random.randint(0,self.yMax)]
        for j in range(len(rockList)):
          #print("x", rockLoc[0], rockList[j][0])
          #print("y", rockLoc[1], rockList[j][1])
          if (rockLoc[0]==rockList[j][0]) and (rockLoc[1]==rockList[j][1]):
            sameRock = True
            #print("rock same position")
            break
        if sameRock == False:
          rockList.append(rockLoc) 
      
      sense.set_pixel(rockList[i][0], rockList[i][1], self.rockColor)
      self.availPoints-=1
  
  def explode(self):
    radius = [self.loX, self.loY]
    exploXLoc, exploYLoc = [radius[0]], [radius[1]]
    
    if radius[0]-1 >= 0:
      exploXLoc.append(radius[0]-1)
      
    if radius[0]+1 <= self.xMax:
      exploXLoc.append(radius[0]+1)
      
    if radius[1]-1 >= 0:  
      exploYLoc.append(radius[1]-1)
      
    if radius[1]+1 <= self.yMax:
       exploYLoc.append(radius[1]+1)
    
    for i in exploXLoc:
      for j in exploYLoc:
        if (radius[0]!=i or radius[1]!=j):
          sense.set_pixel(i, j, self.explodeColor)
        

  def winRound(self):
    sense.show_message("You Won! Next Round", scroll_speed = 0.0000001)
    self.count+=1
    self.availPoints = (self.xMax+1)*(self.yMax+1)
    self.createField()
        
  def lose(self):
    self.explode()
    time.sleep(4)
    sense.show_message("You crashed into a rock and exploded. You Lose :(", scroll_speed=0.00000001)

sense = SenseHat()
sense.clear()
mowing = mowing(sense)
mowing.lawnMower()
