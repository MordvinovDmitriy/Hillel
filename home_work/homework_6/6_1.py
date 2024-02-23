#!/usr/bin/python3

raw_str = input('Введіть ціле додатне число:')
if raw_str.isdigit() and int(raw_str) > 0:
    n = int(raw_str)
else:
    print('not digit')
    raise SystemExit
count = 1
result = 0

while count <= n:
    if count % 3 != 0:
        result = result + count**3
    count += 1
print(f'while: {result}')

result = 0
for count in range(1, n+1):
    if count % 3 != 0:
        result = result + count ** 3
print(f'for: {result}')
