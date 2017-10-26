from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0}        roll {1}         yaw {2}".format(pitch, roll, yaw))
    time.sleep(.5)
    sense.clear()
