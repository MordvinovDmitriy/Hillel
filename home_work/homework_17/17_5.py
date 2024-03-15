#!/usr/bin/python3

class Car(object):
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = Car.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS
        if color not in Car.COLORS:
            Car.COLORS.append(color)

    @classmethod
    def car_fuel_types(cls):
        return cls.FUEL_TYPES

    @staticmethod
    def is_valid_fuel_type(fuel_types_value, c_fuel_types=None):
        if c_fuel_types is None:
            c_fuel_types = Car.car_fuel_types()
        if fuel_types_value in c_fuel_types:
            return fuel_types_value
        else:
            return Car.FUEL_TYPES[0]

    def __str__(self):
        return f'model:{self.model} year:{self.year} color:{self.color} fuel_type:{self.fuel_type}'

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @property
    def numbers(self):
        return f'{self.number} from {self.get_number_of_cars()}'


car_1 = Car('Zaz', 1979, 'black', 'дизель')

car_2 = Car('BMW', 2000, 'red', 'бензин',)

car_3 = Car('VOLVO', 2012, 'black', 'електрикаcccc' )

car_4 = Car('Mercedes', 2012, 'blue', 'гібрид')

print('COLORS:', Car.get_used_colors())
#
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):

    print('item:', item)

    print('numbers:', item.numbers)
