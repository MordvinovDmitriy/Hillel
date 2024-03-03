#!/usr/bin/python3

import json
import csv
from random import randint

def random_number():
    pref_list = ['(095)', '(066)', '(098)', '(096)', '(050)', '(097)']
    phone_yn = randint(1, 100)
    if phone_yn <= 75:
        random_pref = randint(0, 5)
        random_body = str(randint(1000000, 9999999))
        random_n = pref_list[random_pref]+random_body[0:3]+'-'+random_body[3:5]+'-'+random_body[5:7]
        return random_n
    else:
        return 'Номер відсутній'


with open('inp.json', 'r') as file_json:
    json_data = json.load(file_json)

csv_list = []
for key, value in json_data.items():
    csv_data = {}
    csv_data.update({'ID': key, 'Ім\'я': value[0], 'Вік': value[1], 'Телефон': random_number()})
    csv_list.append(csv_data)

header = [keys for keys in csv_list[0].keys()]
print(header)
with open('json2csv.csv', 'w', newline='') as file_csv:
    file_writer = csv.writer(file_csv, delimiter=';')
    file_writer.writerow(header)
    for item in csv_list:
        values = []
        for key in header:
            values.append(item.get(key))
        file_writer.writerow(values)

print(csv_list)
