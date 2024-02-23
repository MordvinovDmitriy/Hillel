#!/usr/bin/python3

def recogn_num(num):
    print(list(num))
    print((float(num)))
    dec_list = ['.', '.']
    if num == '0':
        ret_str = 'Ви ввели нуль'
    elif num.isdigit():
        ret_str = f'Ви ввели позитивне ціле число: {int(num)}'
    elif num[0] == '-' and num[1:].isdigit():
        ret_str = f'Ви ввели від\'ємне ціле число: {int(num)}'
    elif num[0] == '-' and num[1] in dec_list and any(item in dec_list for item in list(num)) and (float(num)):
        ret_str = f'Ви ввели від\'ємне дробове число: {float("-0"+num[1:])}'
    elif num[0] == '-' and any(item in dec_list for item in list(num)) and (float(num)):
        ret_str = f'Ви ввели від\'ємне дробове число: {num}'
    elif any(item in dec_list for item in list(num)) and (float(num)):
        ret_str = f'Ви ввели позитивне дробове число: {float(num)}'
    else:
        ret_str = f'Ви ввели некоректне число: {num}'
    return ret_str


inp_str = ()
exit_var = ["вихід", "exit", "quit", "e", "q"]
while inp_str not in exit_var:

    inp_str = input('Введіть строку: ').lower()
    print(recogn_num(inp_str))
