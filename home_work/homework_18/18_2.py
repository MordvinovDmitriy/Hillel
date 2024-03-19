#!/usr/bin/python3

def generator(from_n=-2, step=-5):
    curr_n = from_n
    while True:
        yield curr_n
        curr_n = curr_n * step


my_gen = generator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print('*' * 50)
my_gen2 = generator(10, 3)
print(next(my_gen2))
print(next(my_gen2))
print(next(my_gen2))
print(next(my_gen2))
print(next(my_gen2))
print(next(my_gen2))
