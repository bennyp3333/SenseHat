from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]

pitchSum = 0
rollSum = 0
yawSum = 0

pitchAverage = pitch
rollAverage = roll
yawAverage = yaw

n = 0
tol = 50

while True:
    n = n + 1
    
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    if(pitch > tol+pitchAverage or pitch < pitchAverage-tol or roll > tol+rollAverage or roll < rollAverage-tol or yaw > tol+yawAverage or yaw < yawAverage-tol):
        print("ive been ashaken!!!")
        n = 1
        pitchSum = 0
        rollSum = 0
        yawSum = 0
##        pitchAverage = pitch
##        rollAverage = roll
##        yawAverage = yaw
    else:
        pitchSum = pitchSum + pitch
        pitchAverage = pitchSum / n
        
        rollSum = rollSum + roll
        rollAverage = rollSum / n
        
        yawSum =yawSum + yaw
        yawAverage = yawSum / n
    
    
    
    print("{3} -- pitch {0}        roll {1}         yaw {2}".format(pitch, roll, yaw, n))
    print("pitch AV--{0}        roll AV--{1}         yaw AV--{2}".format(pitchAverage, rollAverage, yawAverage))
    time.sleep(.5)
