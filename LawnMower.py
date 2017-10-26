from sense_hat import SenseHat
import time
<<<<<<< HEAD
  
# max rgb values are [248,252,248]
  
def lawnMower():
  sense = SenseHat()
  sense.clear()
  
  moveThresh = 30
  grassColor = [0,252,0]
  
  temp = sense.get_temperature()
  for i in range(0,8):
    for j in range(0,8):
      sense.set_pixel(i,j, grassColor)
      
  lastX = 0
  lastY = 7
  loX = 0
  loY = 7
  points = 0
  sense.set_pixel(loX, loY, [248, 0, 32])
  
  while(True):
    orient = sense.get_orientation()
    x = orient["pitch"]
    y = orient["roll"]
    
    if (y > moveThresh and y < 180 and (loY < 7)):
      if(sense.get_pixel(loX, loY+1)==grassColor):
        points+=1
      loY = lastY+1
    elif(y < 360 - moveThresh and y > 180 and (loY>0)):
      if(sense.get_pixel(loX, loY-1)==grassColor):
        points+=1
      loY = lastY-1
    if (x > moveThresh and x < 180 and (loX>0)):
      if(sense.get_pixel(loX-1, loY)==grassColor):
        points+=1
      loX = lastX-1
    elif (x < 360 - moveThresh and x > 180 and (loX<7)):
      if(sense.get_pixel(loX+1, loY)==grassColor):
        points+=1
      loX = lastX+1
      
    sense.set_pixel(lastX, lastY, [2, 255, 119])
    lastX = loX
    lastY = loY
    sense.set_pixel(loX, loY, [255, 2, 36])
    if(points == 64):
      print("You Won!")
    print(points)
    #print(x, y, temp)
    
    time.sleep(1)
lawnMower()
=======

sense = SenseHat()
sense.clear()

moveThresh = 30

temp = sense.get_temperature()



for i in range(0,8):
  for j in range(0,8):
    sense.set_pixel(i,j, [0,255,0])
    
loX = 0
loY = 7
sense.set_pixel(loX, loY, [255, 255, 255])

while(True):
    orient = sense.get_orientation()
    x = orient["pitch"]
    y = orient["roll"]
    z = orient["yaw"]
  
    if (y > moveThresh and y < 180):
        print("blah")
        loY += 1
    elif (y < 360 - moveThresh and y > 180):
        print("meh")
        loY -= 1
    if (x > moveThresh and x < 180):
        print("yes")
        loX -= 1
    elif (x < 360 - moveThresh and x > 180):
        print("nah")
        loX += 1
    
    sense.set_pixel(loX, loY, [255, 255, 255])
    #print(x, " ", y, " ", z)
    print("pitch: {0}        roll: {1}         yaw: {2}".format(x, y, z))
  
    time.sleep(1)
>>>>>>> 1e2ec8abf6741363a1c58dcbfdbadb055d619d35
