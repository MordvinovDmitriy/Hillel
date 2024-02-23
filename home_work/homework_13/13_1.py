#!/usr/bin/python3
from random import randint
from datetime import datetime


def time_decorator(func):
    def wrapper():
        now = datetime.now()
        func()
        print(f'Час виконання функції {func.__name__} {datetime.now()-now}')
    return wrapper


@time_decorator
def random_number():
    return print(randint(1, 100))


@time_decorator
def div_number(a=5, b=4):
    return print(a/b)


random_number()
div_number()
