#!/usr/bin/python3

a = 1, 2
b = 1, 2
print('a == b', a == b)
print('a is b', a is b)
print('-' * 100)
a = set(a)
b = set(b)
print('a == b', a == b)
print('a is b', a is b)
