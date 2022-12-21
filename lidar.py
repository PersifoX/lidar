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

"""
Если вы собрали все правильно, лидар будет возвращать массив с 30-ю элементами типа int
от 0 (лидар не видит препятствия) до 2249 (~22,5 см) 

Основной класс имеет 2 необязательных параметра:
    -DualMode:
        Следует ли лидару инициализировать сразу 2 датчика (Инфакрасный и Ультразвуковой)
        (По умолчанию лидар использует только Ультразвуковой)
    -Debug:
        Выводить ли элементы массива на экран ev3 (поочередно)
"""

class Lidar:

    #read params
    def __init__(self, DualMode:bool=None, Debug:bool=None):

        self.DualMode = DualMode
        self.Debug    = Debug

    #base function for get array of landscape
    def scan(self):
        while True:

            #array of map
            map      = []

            #set null pos
            Motor.run_angle(-200, 60)

            #record map
            i = 0
            while i < 30:

                map.append(UltraSonic.distance())

                #if lidar doesn't see anything
                if map[i] == 2550:
                    map[i] = 0

                if self.Debug == True:
                    ev3.screen.print(map[i])

                Motor.run_angle(30, 4)

                ev3.screen.clear()

                i += 1
            
            
            #end of cycle
            ev3.speaker.beep()
            wait(100)
            ev3.speaker.beep()
            
            #return to null pos
            Motor.run_angle(-200, 60)


            
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

