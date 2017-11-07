from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

class SpaceShip:
  
  def __init__(self, xMax, yMax, enemy):
    self.enemy = enemy
    self.locX, self.locY = int((xMax)/2), yMax
    self.lastX, self.lastY = self.locX, self.locY
    self.color = [248, 252, 248]
    
  def fire(self):
    return Missile(self)

class Missile:
  
  color = [248, 252, 248]

  def __init__(self, ship):
    if ship.enemy==False: #assume enemies will attack down
      self.modify = 1
    else:
      self.modify = -1
    self.ship = ship
    self.locX, self.locY = ship.locX, ship.locY+self.modify
    self.lastX, self.lastY = self.locX, self.locY
    
    
spaceColor = [10,10,10]
xMin, xMax, yMin, yMax = 0, 7, 0, 7

missileList = []
ship = SpaceShip(xMax, yMax, False)
sense = SenseHat()

for i in range(xMax+1):
  for j in range(yMax+1):
    sense.set_pixel(i, j, spaceColor)
    
sense.set_pixel(ship.locX, ship.locY, ship.color)

while(True):
  for command in sense.stick.get_events():
  #using held breaks so far
    print(command.direction)
    if (command.action == "pressed" and command.direction == "left" and ship.locX > xMin):
      print("yes")
      ship.locX-=1
    elif (command.action == "pressed" and command.direction == "right" and ship.locX < xMax):
      print("blah")
      ship.locX+=1
    elif (command.action == "pressed" and command.direction == "middle"):
      print("yes")
      missileList.append(ship.fire())
      curMiss = missileList[len(missileList)]
      sense.set_pixel(curMiss.locX, curMiss.locY, Missile.color)
      
    
    time.sleep(0.1)
      
      
  sense.set_pixel(ship.lastX, ship.lastY, spaceColor)
  ship.lastX, ship.lastY = ship.locX, ship.locY
  sense.set_pixel(ship.locX, ship.locY, ship.color)
  #print("got here")
  
    
  time.sleep(0.4)
    
