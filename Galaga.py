from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

class SpaceShip:
  
  def __init__(self, x_start, y_start, enemy, mult):
    self.enemy = enemy
    self.x_loc, self.y_loc = x_start, y_start
    self.last_x, self.last_y = self.x_loc, self.y_loc
    self.color = [248, 252, 248]
    self.hp = 10*(int(0.5*mult)+1)
    
  def fire(self, damage): #damage as parameter temporary
    return Missile(self, damage)

class Missile:
  
  color = [248, 252, 248]

  def __init__(self, ship, damage):
    if ship.enemy==False: #assume enemies will attack down
      self.modify = -1
    elif ship.enemy==True:
      self.modify = 1
    self.damage = damage
    self.ship = ship
    self.x_loc, self.y_loc = ship.x_loc, ship.y_loc+self.modify
    self.last_x, self.last_y = self.x_loc, self.y_loc
    
    
def shift(sense, item, space_color):
  sense.set_pixel(item.last_x, item.last_y, space_color)
  item.last_x, item.last_y = item.x_loc, item.y_loc
  sense.set_pixel(item.x_loc, item.y_loc, [0, 252, 0])
  
def collision(missiles, fighters): #checks if missile hits
  hit_list = []
  for missile in missiles:
    #moveCheck = missile.y_loc+missile.modify
    for ship in fighters:
      if ship.x_loc == missile.x_loc and ship.y_loc == missile.y_loc:
        hit_info = [ship, missile]
        #print(hit_info[0].hp)
        hit_list.append(hit_info)
  
  return hit_list

def main():      
  space_color = [20,20,20]
  xMin, xMax, yMin, yMax = 0, 7, 0, 7
  
  fighters = []
  missileList = []
  ship = SpaceShip(int((xMax)/2), yMax, False, 1)
  fighters.append(ship) #first index always player
  sense = SenseHat()
  
  for i in range(5):
    randX, randY = random.randint(xMin+1, xMax-1), random.randint(yMin+1, yMax-2)
    curShip = SpaceShip(randX, randY, True, 1)
    #print ("yes", curShip.x_loc, curShip.y_loc)
    sense.set_pixel(curShip.x_loc, curShip.y_loc, [0,252,0])
    #print(curShip.hp)
    fighters.append(curShip)
  
  for i in range(xMax+1):
    for j in range(yMax+1):
      sense.set_pixel(i, j, space_color)
      
  #sense.set_pixel(ship.x_loc, ship.y_loc, ship.color)
  #shift(sense, ship, space_color)
    
  while(True):
    for event in sense.stick.get_events(): #using held breaks so far
      #print(command.direction)
      if event.action == "pressed":
        if event.direction == "left" and ship.x_loc > xMin:
          print("yesl")
          fighters[0].x_loc-=1
        elif event.direction == "right" and ship.x_loc < xMax:
          print ("blah")
          fighters[0].x_loc+=1
        elif event.direction == "up":
          print ("yes")
          curMiss = fighters[0].fire(5)
          missileList.append(curMiss)
          sense.set_pixel(curMiss.x_loc, curMiss.y_loc, Missile.color)
          
      elif event.action == "held":
        print ('held')
        break
      
      #shift(sense,ship, space_color)  
      #time.sleep(0.1)
      
    for ship in fighters: #moves the ships
      #print(ship.enemy, ship.x_loc, ship.y_loc)
      shift(sense, ship, space_color)
      
    for missile in missileList: #moves the missiles
      if missile.y_loc-1 >= yMin and missile.y_loc+1 <= yMax:
        missile.y_loc+=missile.modify
        shift(sense, missile, space_color)
      else:
        sense.set_pixel(missile.x_loc, missile.y_loc, space_color)
        missileList.remove(missile)
        
    for hit_info in collision(missileList, fighters):
      print(hit_info[0].hp, hit_info[1].damage)
      hit_info[0].hp -= hit_info[1].damage
      missileList.remove(hit_info[1])
      if hit_info[0].hp <= 0:
        fighters.remove(hit_info[0])
        sense.set_pixel(hit_info[0].x_loc, hit_info[0].y_loc, space_color)
    
    #sense.set_pixel(ship.last_x, ship.last_y, space_color)
    #ship.last_x, ship.last_y = ship.x_loc, ship.y_loc
    #sense.set_pixel(ship.x_loc, ship.y_loc, ship.color)
    #print("got here")
    
      
    time.sleep(1)
    
    
main()
      
