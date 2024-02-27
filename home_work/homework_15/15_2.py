#!/usr/bin/python3

i = 1
inp_dict = []
while i < 5:
    inp_str = input(f'Введіть {i} строку:')
    if len(inp_str) == 0:
        continue
    inp_dict.append(inp_str)
    i += 1
inp_line1 = inp_dict[0]+'\n'
inp_line2 = inp_dict[1]+'\n'
inp_line3 = inp_dict[2]+'\n'
inp_line4 = inp_dict[3]

file = open('test.txt', 'w')
file.write(inp_line1 + inp_line2)
file.close()

with open('test.txt', 'a') as file:
    file.write(inp_line3 + inp_line4)

