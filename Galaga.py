from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

spaceColor = [0,0,0]

spaceShip = Ship()
sense = SenseHat()

while(True):
  command = sense.stick.get_events()
  
  if (command.direction == "left"):
    print("yes")
  elif (command.direction == "right"):
    print("blah")
    
  if (command.action == "pressed"):
    
class Ship:
  
  def __init__(self):
    self.shipLocX, self.shipLocY = 0, 7
    self.shipLastX, self.shipLastY = self.shipLastX, self.shipLastY
    self.shipColor = [248, 252, 248]
