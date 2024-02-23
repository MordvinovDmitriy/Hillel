#!/usr/bin/python3
from random import randint


def random_number():
    random_n = randint(1, 10)
    return random_n


def new_number():
    raw_str = input('Введіть ціле додатне число від 1 до 10:')
    try:
        int_number = int(raw_str)
        if 0 < int_number <= 10:
            return int_number
    except ValueError:
        return new_number()


def comp_number(a, b):
    ret_str = 'Загадане число більше за вказане' if a > b else 'Загадане число менше за вказане'
    return ret_str


again_var = ['Y', 'y']
attempts = 3

while True:
    if attempts == 0:
        if input('Не залишилось спроб, бажаєте зіграти ще раз?(Y)') in again_var:
            attempts = 3
            continue
        else:
            break
    elif attempts == 3:
            new_rn = random_number()
            new_num = new_number()
            attempts -= 1
    print(new_rn, new_num)
    if new_rn != new_num:
        new_comp = comp_number(new_rn, new_num)
        print(f'{new_comp}, залишилось {attempts} спроб.')
        attempts -= 1
        new_num = new_number()
    else:
        if input('Ви виграли, бажаєте зіграти ще раз?(Y)') in again_var:
            attempts = 3
            continue
        else:
            break


    print(attempts)