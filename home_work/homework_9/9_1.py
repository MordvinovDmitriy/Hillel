#!/usr/bin/python3
from random import randint

def random_number():
    random_n = randint(1, 10)
    return random_n


initial_list = []
final_dict = {}
i = 0
while i < 200:
    initial_list.append(random_number())
    i += 1

for i in initial_list:
    if not final_dict.get(i):
        final_dict[i] = 1
    else:
        final_dict[i] += 1

print(final_dict)
print(dict(sorted(final_dict.items(), key=lambda v: v[0])))
for k, v in dict(sorted(final_dict.items(), key=lambda v: v[0])).items():
    if str(v)[-1] in (2, 3, 4):
        print(str(v) + ' ' + str(v)[-1])
    else:
        str(v)
    print(f'Число {k} зустрічається у первісному списку {v} {(lambda a: "раз" if str(a)[-1] == "1" and a != 11 else "рази" if str(a)[-1] in ("2","3","4") and a not in ("12","13","14") else "разів")(v)}')
