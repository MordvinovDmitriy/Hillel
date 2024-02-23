#!/usr/bin/python3
from random import randint


def random_number():
    random_n = randint(1, 10)
    return random_n


def new_number():
    raw_str = input('Введіть ціле додатне число від 1 до 10:')
    try:
        int_number = int(raw_str)
        if int_number > 0 and int_number < 10:
            return int_number
    except ValueError:
        return new_number()
        # return print('Введіть число')


try_var = ['Y', 'y', 'Д', 'д']
attempts = 3

while True:
    new_rn = random_number()
    new_num = new_number()
    print(new_rn)
    while new_rn != new_num:
        # print(new_rn)
        # if new_rn == new_num:
        #     print('Ви виграли, бажаєте зіграти ще раз?')
        # else:
        attempts -= 1
        if attempts == 0:
            attempts = 3
            break
        print(f'Не вгадали, залишилось {attempts} спроби')
        new_num = new_number()
    else:
        if input('Ви виграли, бажаєте зіграти ще раз?(Д/Y)') in try_var:
            continue





