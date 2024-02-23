#!/usr/bin/python3
import copy

a = ['1']
b = copy.deepcopy(a)

print('a == b', a == b)
print('a is b', a is b)
print('a id is', id(a))
print('b id is', id(b))
print(type(a))
print(type(b))
print('-' * 100)


a = str(a[0])
b = str(b[0])

print('a == b', a == b)
print('a is b', a is b)
print('id(a) is', id(a))
print('id(b) is', id(b))
print(type(a))
print(type(b))
