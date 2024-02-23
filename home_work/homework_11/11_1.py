#!/usr/bin/python3

values = [1, 2, '3', 'forth', 'end', 99, True, None]
new_values = list(map(lambda x: str(x) if type(x) is int else x, values))
print(new_values)
