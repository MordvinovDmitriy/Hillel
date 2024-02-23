#!/usr/bin/python3

inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')
outputdata = list(filter(lambda x:  str(x.lower()) == str(x[::-1].lower()), inputdata))
print(outputdata)
