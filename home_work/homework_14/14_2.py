#!/usr/bin/python3

def recogn_num(num):
    ret_str = f'Ви ввели некоректне число: {num}'
    num = num.replace(",", ".")
    sep_pos = num.find('.')
    if num == '0':
        ret_str = 'Ви ввели нуль'
    elif len(num) > 0:
        if len(num) > 1 and num[0] == '-' and num.count('.') <= 1:
            if num[1:].isdigit():
                ret_str = f'Ви ввели від\'ємне ціле число: {int(num)}'
            elif num[1] == '.' and num[2:].isdigit() and len(num) > 2:
                ret_str = f'Ви ввели від\'ємне дробове число: {float("-0" + num[1:])}'
            elif num[1:sep_pos].isdigit() and num[sep_pos + 1:].isdigit():
                ret_str = f'Ви ввели від\'ємне дробове число: {float(num)}'
        elif num.isdigit():
            ret_str = f'Ви ввели позитивне ціле число: {int(num)}'
        elif num.count('.') == 1 and num[:sep_pos].isdigit() and num[sep_pos + 1:].isdigit():
            ret_str = f'Ви ввели позитивне дробове число: {float(num)}'
        elif num[0] == '.' and num[1:].isdigit():
            ret_str = f'Ви ввели позитивне дробове число: {float("0"+num)}'
    return ret_str


inp_str = ()
exit_var = ["вихід", "exit", "quit", "e", "q"]
while True:
    inp_str = input('Введіть строку: ').lower()
    if inp_str in exit_var:
        break
    else:
        print(recogn_num(inp_str))
