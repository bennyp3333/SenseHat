from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
while(True):
    event = sense.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction))
    sleep(0.1)
    event = sense.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction))
