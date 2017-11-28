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
    self.damage = 20 #amount of damage when run into another ship
    if (self.enemy == True):
      self.color = [0, 252, 248]
    else:
      self.color = [248, 252, 248]
    
  def fire(self, damage): #damage as parameter temporary
    return Missile(self, damage)

class Missile:

  def __init__(self, ship, damage):
    if ship.enemy==False: #assume enemies will attack down
      self.modify = -1
      self.color = [120, 0, 248]
      
    elif ship.enemy==True:
      self.modify = 1
      self.color = [248, 0, 0]
    self.damage = damage
    self.ship = ship
    self.x_loc, self.y_loc = ship.x_loc, ship.y_loc+self.modify
    self.last_x, self.last_y = self.x_loc, self.y_loc
    
    
    
class Game:
  sense = SenseHat()
  space_color = [5, 5, 5]
  x_min, x_max, y_min, y_max = 0, 7, 0, 7
  fighters, enemies, missile_list = [], [], []
  form = random.randint(0,3)
  
  def create_field():
    Game.fighters, Game.enemies, Game.missile_list = [], [], []
    Game.form = random.randint(0,3)
    for i in range(Game.x_max+1): #sets background
      for j in range(Game.y_max+1):
        Game.sense.set_pixel(i, j, Game.space_color)
    
    ship = SpaceShip(int((Game.x_max)/2), Game.y_max, False, 1)
    Game.fighters.append(ship) #first index always player
    Game.sense.set_pixel(Game.fighters[0].x_loc, Game.fighters[0].y_loc, Game.fighters[0].color)
    
    for ship_loc in Game.formation(Game.form, int(Game.x_max/2), int(Game.y_max/2-1)): #sets ship to an intial formation
      #randX, randY = random.randint(x_min+1, x_max-1), random.randint(y_min+1, y_max-2)
      cur_ship = SpaceShip(ship_loc[0], ship_loc[1], True, 1)
      Game.sense.set_pixel(cur_ship.x_loc, cur_ship.y_loc, cur_ship.color)
      Game.fighters.append(cur_ship)
      Game.enemies.append(cur_ship)
    
  def shift(item): #not working anymore
    Game.sense.set_pixel(item.last_x, item.last_y, Game.space_color)
    item.last_x, item.last_y = item.x_loc, item.y_loc
    Game.sense.set_pixel(item.x_loc, item.y_loc, item.color)
    
  def collision(): #checks if missile hits
    hit_list = []
    for missile in Game.missile_list:
      #moveCheck = missile.y_loc+missile.modify
      #past_player = False
      for ship in Game.fighters:
        if ship.x_loc==missile.x_loc and ship.y_loc==missile.y_loc:
          #print(hit_info[0].hp)
          hit_list.append([ship, missile])
          past_player = True
        #elif past_player==True and ship.x_loc==fighters[0].x_loc and ship.y_loc==fighters[0].y_loc:
        #  hit_list.append([fighters[0], ship])
    
    return hit_list
    
  def formation(form_num, x_origin, y_origin):
    ship_form = []
    origin = [x_origin, y_origin]
    ship_form.append(origin)
    #only add if within range
    if form_num == 0 and origin[0]+2<=7 and origin[0]-2>=0 and origin[1]>=1 and origin[1]<=6: #can set x and y max/min to variables
      #print('blah')
      ship_form.append([origin[0]+2, origin[1]])
      ship_form.append([origin[0]-2, origin[1]])
      ship_form.append([origin[0]+1, origin[1]-1])
      ship_form.append([origin[0]-1, origin[1]-1])
    elif form_num == 1 and origin[0]+3<=7 and origin[0]-3>=0 and origin[1]>=1 and origin[1]<=6:
      ship_form.append([origin[0]+2, origin[1]])
      ship_form.append([origin[0]-2, origin[1]])
      ship_form.append([origin[0]+3, origin[1]-1])
      ship_form.append([origin[0]-3, origin[1]-1])
      #print()
    elif form_num == 2 and origin[0]+3<=7 and origin[0]-3>=0 and origin[1]>=1 and origin[1]+1<=6:
      ship_form.append([origin[0]+3, origin[1]])
      ship_form.append([origin[0]-3, origin[1]])
      ship_form.append([origin[0]+1, origin[1]+1])
      ship_form.append([origin[0]-1, origin[1]+1])
      #print()
    elif form_num == 3 and origin[0]+2<=7 and origin[0]-2>=0 and origin[1]>=1 and origin[1]+1<=6:
      ship_form.append([origin[0]+1, origin[1]-1])
      ship_form.append([origin[0]-1, origin[1]-1])
      ship_form.append([origin[0]+2, origin[1]+1])
      ship_form.append([origin[0]-2, origin[1]+1])
      #print('y')
    
    return ship_form
  
  
  def main(): 
    Game.create_field()
    enemy_direction = [True, False] #true means shift right and also up, enemies by default go right and down
    count = 0

    while(True):
      for event in Game.sense.stick.get_events(): #using held breaks so far
        #print(command.direction)
        if event.action == 'pressed':
          if event.direction == 'left' and Game.fighters[0].x_loc > Game.x_min:
            #print('yesl')
            Game.fighters[0].x_loc-=1
          elif event.direction == 'right' and Game.fighters[0].x_loc < Game.x_max:
            #print ('blah')
            Game.fighters[0].x_loc+=1
          elif event.direction == 'up':
            #print ('yes')
            cur_miss = Game.fighters[0].fire(5)
            Game.missile_list.append(cur_miss)
            Game.sense.set_pixel(cur_miss.x_loc, cur_miss.y_loc, cur_miss.color)
            
        #elif event.action == 'held':
        #  print ('held')
        #  break
        
        #shift(sense, fighters[0], space_color)  
        Game.sense.set_pixel(Game.fighters[0].last_x, Game.fighters[0].last_y, Game.space_color)
        Game.fighters[0].last_x, Game.fighters[0].last_y = Game.fighters[0].x_loc, Game.fighters[0].y_loc
        Game.sense.set_pixel(Game.fighters[0].x_loc, Game.fighters[0].y_loc, Game.fighters[0].color)
      
      time.sleep(0.01)
      count+=1
        
      if count%50==0:
        if count == 150: #moves one third of missile auto speed
          #enemies[0] is the origin of the formation
          x_left = Game.formation(Game.form, Game.enemies[0].x_loc-1, Game.enemies[0].y_loc)
          x_right = Game.formation(Game.form, Game.enemies[0].x_loc+1, Game.enemies[0].y_loc)
          y_up = Game.formation(Game.form, Game.enemies[0].x_loc, Game.enemies[0].y_loc-1)
          y_down = Game.formation(Game.form, Game.enemies[0].x_loc, Game.enemies[0].y_loc+1)
          #print(len(x_left), len(x_right), len(y_down))
          if enemy_direction[0]==True and len(x_right)!=1:
            shift = x_right
          elif enemy_direction[0]==True and len(x_right)==1:
            enemy_direction[0] = not enemy_direction[0]
            #shift = y_down
            
            if enemy_direction[1]==False and len(y_down)!=1:
              shift = y_down
            elif enemy_direction[1]==False and len(y_down)==1:
              enemy_direction[1] = not enemy_direction[1]
              shift = y_up
            elif enemy_direction[1]==True and len(y_up)!=1:
              shift = y_up
            elif enemy_direction[1]==True and len(y_up)==1:
              enemy_direction[1] = not enemy_direction[1]
              shift = y_down
            
          elif enemy_direction[0]==False and len(x_left)!=1:
            shift = x_left
          elif enemy_direction[0]==False and len(x_left)==1:
            enemy_direction[0] = not enemy_direction[0]
            #shift = y_down
            
            if enemy_direction[1]==False and len(y_down)!=1:
              shift = y_down
            elif enemy_direction[1]==False and len(y_down)==1:
              enemy_direction[1] = not enemy_direction[1]
              shift = y_up
            elif enemy_direction[1]==True and len(y_up)!=1:
              shift = y_up
            elif enemy_direction[1]==True and len(y_up)==1:
              enemy_direction[1] = not enemy_direction[1]
              shift = y_down
            
          for i in range(len(Game.enemies)): #moves the enemy ships
            #print(shift[i][0], shift[i][1])
            Game.enemies[i].x_loc, Game.enemies[i].y_loc = shift[i][0], shift[i][1]
            cur_ship = Game.enemies[i]
            #shift(sense, cur_ship, space_color)
            if random.randint(0, 3)==1: #fires missile
              cur_miss = Game.enemies[i].fire(5)
              Game.sense.set_pixel(cur_miss.x_loc, cur_miss.y_loc, cur_miss.color)
              Game.missile_list.append(cur_miss)
            Game.sense.set_pixel(Game.enemies[i].last_x, Game.enemies[i].last_y, Game.space_color)
            Game.enemies[i].last_x, Game.enemies[i].last_y = Game.enemies[i].x_loc, Game.enemies[i].y_loc
            Game.sense.set_pixel(Game.enemies[i].x_loc, Game.enemies[i].y_loc, Game.enemies[i].color)
          
          count = 0
          
        for missile in Game.missile_list: #moves the missiles
          if missile.y_loc-1 >= Game.y_min and missile.y_loc+1 <= Game.y_max:
            missile.y_loc+=missile.modify
            #shift(sense, missile, space_color)
            Game.sense.set_pixel(missile.last_x, missile.last_y, Game.space_color)
            missile.last_x, missile.last_y = missile.x_loc, missile.y_loc
            Game.sense.set_pixel(missile.x_loc, missile.y_loc, missile.color)
          else:
            Game.sense.set_pixel(missile.x_loc, missile.y_loc, Game.space_color)
            Game.missile_list.remove(missile)
            
        for hit_info in Game.collision():
          print(hit_info[0].hp, hit_info[1].damage)
          hit_info[0].hp -= hit_info[1].damage
          Game.missile_list.remove(hit_info[1])
          if hit_info[0].hp <= 0 and hit_info[0].enemy == True: #only removes if an enemy
            try:
              Game.fighters.remove(hit_info[0])
              Game.enemies.remove(hit_info[0])
            except:
              print('yes')
            Game.sense.set_pixel(hit_info[0].x_loc, hit_info[0].y_loc, hit_info[0].color)
            #time.sleep(0.1)
            #Game.sense.set_pixel(hit_info[0].x_loc, hit_info[0].y_loc, Game.space_color)
            
        if Game.fighters[0].hp <= 0:
          Game.sense.show_message("Your ship was destroyed")
          break
        elif len(Game.fighters)==1:
          Game.sense.show_message("All enemies killed, next round")
          Game.create_field()
        
      #sense.set_pixel(ship.last_x, ship.last_y, space_color)
      #ship.last_x, ship.last_y = ship.x_loc, ship.y_loc
      #sense.set_pixel(ship.x_loc, ship.y_loc, ship.color)
      #print('got here')
      
        
      #time.sleep(1)
      
    
Game.main()
