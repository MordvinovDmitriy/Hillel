#!/usr/bin/python3

raw_str = input('Введіть число:')

try:
    inp_int = int(raw_str)
except ValueError:
    print('невірне введення')
    raise SystemExit

number = 'нуль' if inp_int == 0 else 'непарне' if inp_int % 2 else 'парне'
template = f'Ви ввели {number} число'
print(template)
