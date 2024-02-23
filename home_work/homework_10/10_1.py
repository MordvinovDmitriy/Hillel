#!/usr/bin/python3
from random import randint


def random_number():
    random_n = randint(0, 10)
    return random_n


new_rn = random_number()
lam = lambda num: (str(num)+' число нуль') if num == 0 else (str(num)+' непарне число') if num % 2 else (str(num)+' парне число')
print(f'{lam(new_rn)}')
