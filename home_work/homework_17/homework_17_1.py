#!/usr/bin/python3

class auto(object):
    def __init__(self, brand, age, mark, color='red', weight='1244 kg'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def birthday(self):
        self.age += 1

    def move(self):
        print('move')

    def stop(self):
        print('stop')


if __name__ == '__main__':
    honda = auto('honda', 5, 'civic')
    print(honda.__dict__)
    honda.birthday()
    honda.move()
    honda.stop()
    print(honda.__dict__)
