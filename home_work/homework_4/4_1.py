#!/usr/bin/python3

file = open("./output.txt", "w")
raw_string = input('Введіть речення з двох слів: ')
first_word, second_word = raw_string.split()
first_word = first_word.title()
second_word = second_word.upper()

text1 = '!%s %s?' % (second_word, first_word)
text2 = '!{sw} {fw}?'.format(fw=first_word, sw=second_word)
text3 = f'!{second_word} {first_word}?'

print(raw_string, text1, text2, text3, sep='<<<>>>')
print(raw_string, text1, text2, text3, sep='<<<>>>', file=file)
file.close()
