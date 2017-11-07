from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

    
class SpaceShip:
  
  def __init__(self):
    self.xMin, self.xMax, self.yMin, self.yMax = 0, 7, 0, 7
    self.locX, self.locY = int((self.xMin*2)/2), self.yMax
    self.lastX, self.lastY = self.locX, self.locY
    self.color = [248, 252, 248]
    
    
spaceColor = [10,10,10]

ship = SpaceShip()
sense = SenseHat()

for i in range(ship.xMax+1):
  for j in range(ship.yMax+1):
    sense.set_pixel(i, j, spaceColor)
    
sense.set_pixel(ship.locX, ship.locY, ship.color)

while(True):
  command = sense.stick.wait_for_event(emptybuffer=True)
  print(command.direction)
  if (command.direction == "left" and ship.locX > ship.xMin):
    print("yes")
    ship.locX-=1
  elif (command.direction == "right" and ship.locX < ship.xMax):
    print("blah")
    ship.locX+=1
  else:
    print("nothing")
    
  sense.set_pixel(ship.lastX, ship.lastY, spaceColor)
  ship.lastX, ship.lastY = ship.locX, ship.locY
  sense.set_pixel(ship.locX, ship.locY, ship.color)
  print("got here")
    
  if (command.action == "pressed"):
    print("yes")
    
  time.sleep(0.4)
    
