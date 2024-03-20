#!/usr/bin/python3
import datetime

import openpyxl
from openpyxl import Workbook
from datetime import date, datetime
import os.path


class Person(object):
    date_sep = [' ', '.', '/', '-']

    def __init__(self, name, patronymic=None, surname=None, birth_date=None, death_date=None, gender='m', per_sh=None):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.birth_date = Person.is_valid_date(str(birth_date))
        self.death_date = '' if death_date == '' else Person.is_valid_date(str(death_date))
        self.gender = Person.is_valid_gender(gender)
        self.per_sh = per_sh

    def __str__(self):
        return f'{self.name}, {self.patronymic}, {self.surname}, {self.birth_date}, {self.death_date}, {self.gender}'

    @staticmethod
    def is_valid_date(date):
        separator = None
        for items in Person.date_sep:
            if items in date:
                print(separator)
                separator = items
        if separator is not None and date.replace(separator, '').isdigit():
            spl_date = date.split(sep=separator)
            try:
                day = int(spl_date[0])
                month = int(spl_date[1])
                year = int(spl_date[2])
                day_s = spl_date[0] if len(spl_date[0]) > 1 else '0' + spl_date[0]
                month_s = spl_date[1] if len(spl_date[1]) > 1 else '0' + spl_date[1]
                year_s = spl_date[2]
            except IndexError:
                raise Date_exception
            feb_d = 28
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                feb_d += 1
            if day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
                return day_s + '.' + month_s + '.' + year_s
            elif int(spl_date[0]) <= 30 and int(spl_date[1]) in [4, 6, 9, 11]:
                return day_s + '.' + month_s + '.' + year_s
            elif int(spl_date[0]) <= feb_d and int(spl_date[1]) == 2:
                return day_s + '.' + month_s + '.' + year_s
            else:
                raise Date_exception
        else:
            raise Date_exception

    @staticmethod
    def is_valid_gender(gen):
        if gen.lower() in ['f', 'm', 'ж', 'ч']:
            print(gen)
            return gen.lower()
        else:
            print(gen.lower())
            raise Gender_exception

    def age(self):
        if self.death_date is None:
            return date.today() - self.birth_date
        else:
            return death_date - self.birth_date


    def save_person(self):
        s_per = [self.name, self.patronymic, self.surname, self.birth_date, self.death_date, self.gender]
        if self.per_sh.cell(1, 1).value is None:
            max_row_c = 1
        else:
            max_row_c = self.per_sh.max_row+1
        max_col_c = 7
        for i in range(1, max_col_c):
            cell_c = self.per_sh.cell(row=max_row_c, column=i)
            cell_c.value = s_per[i - 1]

        wb.save('./diplom.xlsx')
        wb.close()


class Date_exception(Exception):
    def __init__(self, message='wrong date format'):
        super().__init__(message)


class Gender_exception(Exception):
    def __init__(self, message='only two gender available'):
        super().__init__(message)


if os.path.isfile('./diplom.xlsx'):
    wb = openpyxl.open('./diplom.xlsx')
else:
    wb = Workbook()
    wb.active.title = 'Person'
    wb.save('./diplom.xlsx')
per_sheet = wb['Person']
print(date.today())

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
        except Date_exception:
            print('-'*50)
            print('wrong date format')
            print('-' * 50)
            continue
        except Gender_exception:
            print('-'*50)
            print('wrong gender')
            print('-' * 50)
            continue

        per.save_person()
    if comm_var == 's':
        search_string = input('input search string: ').lower()
        search_list = []
        max_row = per_sheet.max_row+1
        max_column = per_sheet.max_column+1
        format_s = '%d.%m.%Y'
        for row in range(1, max_row):
            row_list = []
            row_dict = {}
            for column in range(1, max_column):
                cell = per_sheet.cell(row, column)
                if column == 1:
                    row_dict['name'] = cell.value
                elif column in [2, 3] and cell.value is not None:
                    row_dict.update({'name': row_dict.get('name') + ' ' + cell.value})
                # elif column == 4 and type(cell.value) is datetime:
                elif column == 4:
                    if type(cell.value) is datetime:
                        print('datetime')
                        row_dict['date_birth'] = cell.value.strftime(format_s)
                    else:
                        print('not datetime')
                        print(cell.number_format)
                        # row_dict['date_birth'] = datetime.strptime(cell.value, format_s).date()
                        row_dict['date_birth'] = cell.value

                elif column == 5:
                    if type(cell.value) is datetime:
                        row_dict['death_date'] = cell.value.strftime(format_s)
                        days = (datetime.strptime(row_dict.get('death_date'), format_s) - datetime.strptime(row_dict.get('date_birth'), format_s)).days
                        row_dict['age'] = int(days / 365)
                    else:
                        row_dict['death_date'] = None
                        print(row_dict.get('date_birth'))
                        days = (datetime.now() - datetime.strptime(row_dict.get('date_birth'), format_s)).days
                        # days = (datetime.now() - row_dict.get('date_birth')).days
                        row_dict['age'] = int(days / 365)
                else:
                    row_dict['gender'] = 'чоловік' if cell.value in ['m', 'м'] else 'жінка'
            search_list.append(row_dict)

        # print(row_dict)
        # print(search_list)
        counter = 0
        for sub in search_list:
            if search_string in sub['name'].lower():
                m_birth, m_death = None, None
                if sub['gender'] == 'чоловік':
                    m_birth = 'Народився'
                    m_death = ', Помер' if sub['death_date'] is not None else ''
                else:
                    m_birth = 'Народилася'
                    m_death = ', Вмерла' if sub['death_date'] is not None else ''
                if sub["death_date"] is None:
                    death_date = ''
                else:
                    death_date = sub["death_date"]
                age_raw_str = str(sub["age"])
                if age_raw_str[-1] == '1' and age_raw_str != '11':
                    age_str = age_raw_str + ' рік'
                elif age_raw_str[-1] in ('2', '3', '4'):
                    age_str = age_raw_str + ' роки'
                else:
                    age_str = age_raw_str + ' років'
                print(f'{sub["name"]} {age_str}, {sub["gender"]}, {m_birth} {sub["date_birth"]}{m_death} {death_date}')
                counter += 1
        if counter == 0:
            print('Not found')
    if comm_var.upper() == exit_var:
        break
