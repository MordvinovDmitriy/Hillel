#!/usr/bin/python3
import copy

a = [1, 2, 3]
b = copy.copy(a)

print('a == b', a == b)
print('a is b', a is b)
print('a id is', id(a))
print('b id is', id(b))
