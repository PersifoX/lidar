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
Infrared   = InfraredSensor(Port.S1)


"""
Если вы собрали все правильно, лидар будет возвращать массив с 30-ю элементами типа int
от 0 (лидар не видит препятствия) до 2249 (~225 см) 

Основной класс имеет 2 необязательных параметра:
    -DualMode:
        Следует ли лидару инициализировать сразу 2 датчика (Инфакрасный и Ультразвуковой)
        (По умолчанию лидар использует только Ультразвуковой)
    -Debug:
        Выводить ли элементы массива на экран ev3 (поочередно)
    -Speed:
        Скорость вращения лидара, чем меньше - тем лучше стабилизация. По умолчанию 30.
"""


class Lidar:

    #read params
    def __init__(self, DualMode:bool=False, Debug:bool=False, Speed:int=30):

        self.DualMode = DualMode
        self.Debug    = Debug
        self.Speed    = Speed

    #base function for get array of landscape
    def scan(self):
        while True:

            #array of map
            UltraMap    = []
            InfraredMap = []

            #set null pos
            Motor.run_angle(-200, 60)

            #record map
            i = 0
            while i < 30:

                UltraMap.append(UltraSonic.distance())

                #if lidar doesn't see anything
                if UltraMap[i] == 2550:
                    UltraMap[i] = 0

                if self.DualMode == True:
                    InfraredMap.append(Infrared.distance())

                if self.Debug == True:
                    ev3.screen.print(str(UltraMap[i]) + " | " + str(InfraredMap[i]))

                Motor.run_angle(self.Speed, 4)

                ev3.screen.clear()

                i += 1
            

            #end of cycle
            ev3.speaker.beep()
            wait(100)
            ev3.speaker.beep()
            
            #return to null pos
            Motor.run_angle(-200, 60)


            if self.DualMode == True:
                return UltraMap, InfraredMap
            else:
                return UltraMap

        
    """def printmap(self):

        i = 0
        #drawing map
        ev3.screen.clear()
        while i < 30:
            x = i * 6

            y = 128 - (UltraMap[i] // 20)

            x2 = (i + 1) * 6
            y2 = 128 - (UltraMap[i + 1] // 20)


            ev3.screen.draw_line(x, y, x2, y2)
            i = i + 1"""



class Tools:

    def __init__(self, OptionalMap:list=None):
        self.OptionalMap = OptionalMap

    def find_longest_zeros(self, map):
        """
            find_longest_zeros возвращает начало start и конец stop
            самой длинной последовательности нулей внутри входной последовательности map

            map - последовательность замеров с лидара, где 0 - не найденная стена, глубокая неизвестность
        """
        leng = 0
        start = 0
        stop = 0

        temp_start = -1
        temp_stop = 0
        temp_len = 0

        
        for idx, item in enumerate(map):
            if item == 0:
                if temp_start == -1:
                    temp_start = idx
                temp_len += 1
            else:
                if temp_start != -1:
                    temp_stop = idx - 1
                if leng < temp_len:
                    leng = temp_len
                    start = temp_start
                    stop = temp_stop
                temp_start = -1
                temp_stop = 0
                temp_len = 0

        return start, stop