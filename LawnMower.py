from sense_hat import SenseHat
import time
  
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
 
  loX, lastX, loY, lastY = 0, 0, 7, 7
  points = 0
  sense.set_pixel(loX, loY, [248, 0, 32])
  
  while(True):
    x = 0
    y = 0
    orient = sense.get_orientation()
    x = orient["pitch"]
    y = orient["roll"]
    print("pitch {0}        roll {1}".format(x, y))
    if (y > moveThresh and y < 180 and loY < 7):
      if(sense.get_pixel(loX, loY+1)==grassColor):
        points+=1
      loY = lastY+1
    elif(y < 360 - moveThresh and y > 180 and loY > 0):
      if(sense.get_pixel(loX, loY-1)==grassColor):
        points+=1
      loY = lastY-1
    else:
        print("no Y change")
    if (x > moveThresh and x < 180 and loX > 0):
      if(sense.get_pixel(loX-1, loY)==grassColor):
        points+=1
      loX = lastX-1
    elif (x < 360 - moveThresh and x > 180 and loX < 7):
      if(sense.get_pixel(loX+1, loY)==grassColor):
        points+=1
      loX = lastX+1
    else:
        print("no X change")
      
    sense.set_pixel(lastX, lastY, [2, 252, 119])
    lastX = loX
    lastY = loY
    sense.set_pixel(loX, loY, [248, 2, 36])
    if(points == 64):
      print("You Won!")
    print(points)
    #print(x, y, temp)
    
    time.sleep(1)

lawnMower()
