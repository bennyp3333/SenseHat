from sense_hat import SenseHat
import time

sense = SenseHat()

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
  print(x, " ", y, " ", temp)
  
  time.sleep(2)
