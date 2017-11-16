from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

class SpaceShip:
  
  def __init__(self, x_start, y_start, enemy, mult):
    self.enemy = enemy
    self.x_loc, self.y_loc = x_start, y_start
    self.last_x, self.last_y = self.x_loc, self.y_loc
    self.hp = 10*(int(0.5*mult)+1)
    if (self.enemy == True):
      self.color = [0, 252, 248]
    else:
      self.color = [248, 252, 248]
    
  def fire(self, damage): #damage as parameter temporary
    return Missile(self, damage)

class Missile:
  color = [248, 0, 0]

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
  sense.set_pixel(item.x_loc, item.y_loc, item.color)
  
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
  sense = SenseHat()
  space_color = [5, 5, 5]
  x_min, x_max, y_min, y_max = 0, 7, 0, 7
  
  for i in range(x_max+1): #sets background
    for j in range(y_max+1):
      sense.set_pixel(i, j, space_color)
  
  fighters, enemies, missile_list = [], [], []
  ship = SpaceShip(int((x_max)/2), y_max, False, 1)
  fighters.append(ship) #first index always player
  
  for i in range(5):
    randX, randY = random.randint(x_min+1, x_max-1), random.randint(y_min+1, y_max-2)
    cur_ship = SpaceShip(randX, randY, True, 1)
    #print ('yes', cur_ship.x_loc, cur_ship.y_loc)
    sense.set_pixel(cur_ship.x_loc, cur_ship.y_loc, cur_ship.color)
    #print(cur_ship.hp)
    fighters.append(cur_ship)
    enemies.append(cur_ship)
      
  sense.set_pixel(fighters[0].x_loc, fighters[0].y_loc, fighters[0].color)
  #shift(sense, ship, space_color)
  
  count = 0
  while(True):
    for event in sense.stick.get_events(): #using held breaks so far
      #print(command.direction)
      if (event.action == 'pressed' or event.action == 'hold'):
        if event.direction == 'left' and fighters[0].x_loc > x_min:
          #print('yesl')
          fighters[0].x_loc-=1
        elif event.direction == 'right' and fighters[0].x_loc < x_max:
          #print ('blah')
          fighters[0].x_loc+=1
        elif event.direction == 'up':
          #print ('yes')
          curMiss = fighters[0].fire(5)
          missile_list.append(curMiss)
          sense.set_pixel(curMiss.x_loc, curMiss.y_loc, Missile.color)
          
      #elif event.action == 'held':
      #  print ('held')
      #  break
      
      shift(sense, fighters[0], space_color)  
    
    time.sleep(0.01)
    count+=1
      
    if count==50:
      count = 0
      for ship in enemies: #moves the enemie ships
        #print(ship.enemy, ship.x_loc, ship.y_loc)
        shift(sense, ship, space_color)
        
      for missile in missile_list: #moves the missiles
        if missile.y_loc-1 >= y_min and missile.y_loc+1 <= y_max:
          missile.y_loc+=missile.modify
          shift(sense, missile, space_color)
        else:
          sense.set_pixel(missile.x_loc, missile.y_loc, space_color)
          missile_list.remove(missile)
          
      for hit_info in collision(missile_list, fighters):
        print(hit_info[0].hp, hit_info[1].damage)
        hit_info[0].hp -= hit_info[1].damage
        missile_list.remove(hit_info[1])
        if hit_info[0].hp <= 0:
          try:
            fighters.remove(hit_info[0])
            if hit_info[0].enemy == True:
              enemies.remove(hit_info[0])
          except:
            print('yes')
          sense.set_pixel(hit_info[0].x_loc, hit_info[0].y_loc, hit_info[1].color)
          time.sleep(0.1)
          sense.set_pixel(hit_info[0].x_loc, hit_info[0].y_loc, space_color)
      
    #sense.set_pixel(ship.last_x, ship.last_y, space_color)
    #ship.last_x, ship.last_y = ship.x_loc, ship.y_loc
    #sense.set_pixel(ship.x_loc, ship.y_loc, ship.color)
    #print('got here')
    
      
    #time.sleep(1)
    
    
main()
