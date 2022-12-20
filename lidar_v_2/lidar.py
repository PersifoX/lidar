#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

UltraSonic = UltrasonicSensor(Port.S4)
#Gyro       = GyroSensor(Port.S1)
Motor      = Motor(Port.D)



class Lidar:

    def scan(self):

        while True:

            #number of cycle
            n = 0

            #array of map
            map      = []
            pointmap = []

            #set null pos
            Motor.run_angle(-200, 60)

            i = 0
            #record map
            while i < 30:

                map.append(UltraSonic.distance())

                if map[i] == 2550:
                    map[i] = 0

                Motor.run_angle(30, 4)


                i = i + 1
            
            

            #ev3.speaker.beep()
            #wait(100)
            #ev3.speaker.beep()
            
            ev3.speaker.play_file("inecraft_death.wav")

            Motor.run_angle(-200, 60)


            print(map)
            
            return map

        
    def printmap(self):

        i = 0
        #drawing map
        ev3.screen.clear()
        while i < 30:
            x = i * 6

            y = 128 - (map[i] // 20)

            x2 = (i + 1) * 6
            y2 = 128 - (map[i + 1] // 20)


            ev3.screen.draw_line(x, y, x2, y2)
            i = i + 1

