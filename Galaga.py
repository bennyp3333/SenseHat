from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

class SpaceShip:
  
  def __init__(self, xStart, yStart, enemy): #use max and min to find start position
    self.enemy = enemy
    self.locX, self.locY = xStart, yStart
    self.lastX, self.lastY = self.locX, self.locY
    self.color = [248, 252, 248]
    
  def fire(self):
    return Missile(self)

class Missile:
  
  color = [248, 252, 248]

  def __init__(self, ship):
    if ship.enemy==False: #assume enemies will attack down
      self.modify = -1
    elif ship.enemy==True:
      self.modify = 1
    self.ship = ship
    self.locX, self.locY = ship.locX, ship.locY+self.modify
    self.lastX, self.lastY = self.locX, self.locY
    
    
def shift(sense, item, spaceColor):
  sense.set_pixel(item.lastX, item.lastY, spaceColor)
  item.lastX, item.lastY = item.locX, item.locY
  sense.set_pixel(item.locX, item.locY, [255,255,255])
  
def collision(missiles, fighters):
  hitList = []
  for missile in missiles:
    moveCheck = missile.locY+missile.modify
    for ship in fighters:
      if ship.locX == missile.locX and ship.locY == moveCheck:
        hitList.append(ship)
    

def main():      
  spaceColor = [20,20,20]
  xMin, xMax, yMin, yMax = 0, 7, 0, 7
  
  fighters = []
  missileList = []
  ship = SpaceShip(int((xMax)/2), yMax, False)
  fighters.append(ship) #first index always player
  sense = SenseHat()
  
  for i in range(5):
    randX, randY = random.randint(xMin+1, xMax-1), random.randint(yMin+1, yMax-2)
    curShip = SpaceShip(randX, randY, True)
    #print ("yes", curShip.locX, curShip.locY)
    sense.set_pixel(curShip.locX, curShip.locY, [0,252,0])
    fighters.append(curShip)
  
  for i in range(xMax+1):
    for j in range(yMax+1):
      sense.set_pixel(i, j, spaceColor)
      
  #sense.set_pixel(ship.locX, ship.locY, ship.color)
  #shift(sense, ship, spaceColor)
    
  while(True):
    for event in sense.stick.get_events(): #using held breaks so far
      #print(command.direction)
      if event.action == "pressed":
        if event.direction == "left" and ship.locX > xMin:
          print("yesl")
          fighters[0].locX-=1
        elif event.direction == "right" and ship.locX < xMax:
          print "blah"
          fighters[0].locX+=1
        elif event.direction == "up":
          print "yes"
          curMiss = fighters[0].fire()
          missileList.append(curMiss)
          sense.set_pixel(curMiss.locX, curMiss.locY, Missile.color)
          
      elif event.action == "held":
        print 'held'
        break
      
      #shift(sense,ship, spaceColor)  
      #time.sleep(0.1)
      
    for ship in fighters:
      print(ship.enemy, ship.locX, ship.locY)
      shift(sense, ship, spaceColor)
      
    for missile in missileList: #need to set bounds
      if missile.locY-1 >= yMin and missile.locY+1 <= yMax:
        missile.locY+=missile.modify
        shift(sense, missile, spaceColor)
      else:
        sense.set_pixel(missile.locX, missile.locY, spaceColor)
        missileList.remove(missile)
        
    #sense.set_pixel(ship.lastX, ship.lastY, spaceColor)
    #ship.lastX, ship.lastY = ship.locX, ship.locY
    #sense.set_pixel(ship.locX, ship.locY, ship.color)
    #print("got here")
    
      
    time.sleep(1)
    
    
main()
      
