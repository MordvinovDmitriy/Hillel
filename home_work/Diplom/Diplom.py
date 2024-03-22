#!/usr/bin/python3

import openpyxl
from openpyxl import Workbook
from person import Person, Gender_exception
import os.path

load = input('Load previously saved data ? y/n ').lower()

if os.path.isfile('./diplom.xlsx') and load == 'n':
    if input('This is overwtite existing file. y/n ').lower() == 'y':
        wb = Workbook()
        wb.active.title = 'Person'
        wb.save('./diplom.xlsx')
    else:
        wb = openpyxl.open('./diplom.xlsx')

elif os.path.isfile('./diplom.xlsx') and load == 'y':
    wb = openpyxl.open('./diplom.xlsx')
else:
    wb = Workbook()
    wb.active.title = 'Person'
    wb.save('./diplom.xlsx')


per_sheet = wb['Person']
per = Person(None, None, None, '01-01-1900', '01-01-1900', 'ж', per_sheet)
exit_var = 'Q'
while True:
    print('press "a" to add person')
    print('press "s" to search')
    print('press "q" quit')
    comm_var = input()
    if comm_var == 'a':
        name = input('Input name: ')
        patronymic = input('Input patronymic: ')
        surname = input('Input surname: ')
        date_birth = input('Input date of birth: ')
        death_date = input('Input date of death if available:')
        gender = input('Input gender f/ж or m/ч:')
        per_sheet = per_sheet
        try:
            per = Person(name, patronymic, surname, date_birth, death_date, gender, per_sheet)
        except ValueError:
            print('-'*50)
            print('wrong date format')
            print('-' * 50)
            continue
        except Gender_exception:
            print('-'*50)
            print('wrong gender')
            print('-' * 50)
            continue

        per.save_person(wb)
    if comm_var == 's':
        search_string = input('input search string: ').lower()
        try:
            per.search_person(search_string)
        except AttributeError:
            print('-'*50)
            print('no records in file')
            print('-'*50)
            continue

    if comm_var.upper() == exit_var:
        break
