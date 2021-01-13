# 엑세서
# EX 2) 보일러 IoT 시스템이서의 엑세서

import time
import random

class TempSensor:
    def __init__(self):
        self.value = 5

    def read_temp(self):
        self.value = random.uniform(0,10) # 해당 범위 내의 랜덤한 실수
        return self.value

class Boiler:
    def on(self):
        print('보일러가 켜집니다.')

class Ligth:
    def on(self):
        print('전등이 켜집니다.')

class Controller:
    def __init__(self, base, func): # 주입 : injection
        self.base = base
        # self.boiler = Boiler()
        self.func = func
        self._temp = 10

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < self.base:
            # self.boiler.on()
            self.func() # 전략 패턴

        self._temp = value


tsensor = TempSensor()
boiler = Boiler()
light = Ligth()

controller = Controller(5, light.on)

# 1초 간격으로 온도 측정
while True:
    controller.temp = tsensor.read_temp()
    print(controller.temp)
    print()
    time.sleep(1)