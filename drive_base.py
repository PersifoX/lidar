#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from lidar import Lidar, Tools

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3   = EV3Brick()
lidar = Lidar()
tools = Tools()

right_motor = Motor(Port.B)
left_motor  = Motor(Port.C)

base = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()

#base.turn(0)
#base.straight(100)




#print(find_longest_zeros(lidar.scan()))

def find_center_zeros_ang(map):
    ang = 0
    start, stop = tools.find_longest_zeros(map)
    
    if start > 15:
        napr = 1
    else:
        napr = -1
    center_zeros = int((start + stop) / 2)
    
    ang = (start + center_zeros) * 2 * napr

    return ang



while True:
    map = lidar.scan()
    ang =  find_center_zeros_ang( map )
    ev3.speaker.beep()
    base.turn(ang)
    base.straight(300)
