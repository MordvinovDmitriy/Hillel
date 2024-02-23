#!/usr/bin/python3

inp = input('Enter string: \n')
parity_str = inp[1::2]
rev_str = inp[-1::-1].upper()
print(parity_str)
print(rev_str)
