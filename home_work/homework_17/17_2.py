#!/usr/bin/python3
import time
from homework_17_1 import auto


class truck(auto):
    def __init__(self, brand, age, mark, max_load, color='red', weight='1244 kg'):
        super().__init__(brand, age, mark, color,weight)
        self.max_load = max_load
    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class car(auto):
    def __init__(self, brand, age, mark, max_speed, color='red', weight='1244 kg'):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed} km/h')


truck_1 = truck('Iveco', 3, 'Daily', '1345 kg', 'white')
truck_1.move()
truck_1.stop()
truck_1.birthday()
truck_1.load()
print(truck_1.__dict__)

truck_2 = truck('Chevrolet', 17, 'Express', '1473 kg')
truck_2.move()
truck_2.stop()
truck_2.birthday()
truck_2.load()
print(truck_2.__dict__)

car_1 = car('Audi', 14, 'A4', 216, 'black')
car_1.move()
car_1.stop()
car_1.birthday()
print(car_1.__dict__)

car_2 = car('Toyota', 5, 'Camry', 220, 'blue','1560 kg')
car_2.move()
car_2.stop()
car_2.birthday()
print(car_2.__dict__)
