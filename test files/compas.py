from sense_hat import SenseHat
import time
sense = SenseHat()

north = sense.get_compass()
while(True):
    north = sense.get_compass()
    print("North: %s" % north)
    time.sleep(0.1)