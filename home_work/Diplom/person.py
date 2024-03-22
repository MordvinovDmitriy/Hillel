from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Person(object):
    date_sep = [' ', '.', '/', '-']

    def __init__(self, name, patronymic=None, surname=None, birth_date=None, death_date=None, gender='m', per_sh=None):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.birth_date = Person.is_valid_date(birth_date)
        self.death_date = '' if death_date == '' else Person.is_valid_date(death_date)
        self.gender = Person.is_valid_gender(gender)
        self.per_sh = per_sh

    def __str__(self):
        return f'{self.name}, {self.patronymic}, {self.surname}, {self.birth_date}, {self.death_date}, {self.gender}'

    @staticmethod
    def is_valid_date(is_date):
        separator = None
        for items in Person.date_sep:
            if items in is_date:
                separator = items
        if separator is None:
            raise ValueError
        else:
            return datetime.strptime(is_date, f'%d{separator}%m{separator}%Y').date().strftime("%d.%m.%Y")

    @staticmethod
    def is_valid_gender(gen):
        if gen.lower() in ['f', 'm', 'ж', 'ч']:
            return gen.lower()
        else:
            raise Gender_exception

    # def age(self):
    #     if self.death_date is None:
    #         return date.today() - self.birth_date
    #     else:
    #         return self.death_date - self.birth_date

    def search_person(self, s_string):
        search_list = []
        max_row = self.per_sh.max_row + 1
        max_column = self.per_sh.max_column + 1
        format_s = '%d.%m.%Y'
        for row in range(1, max_row):
            row_dict = {}
            for column in range(1, max_column):
                cell = self.per_sh.cell(row, column)
                if column == 1:
                    row_dict['name'] = cell.value
                elif column in [2, 3] and cell.value is not None:
                    row_dict.update({'name': row_dict.get('name') + ' ' + cell.value})
                elif column == 4:
                    if type(cell.value) is datetime:
                        row_dict['date_birth'] = cell.value.strftime(format_s)
                    else:
                        row_dict['date_birth'] = cell.value

                elif column == 5:
                    if type(cell.value) is str and cell.value != '':
                        row_dict['death_date'] = cell.value
                        death_datetime = datetime.strptime(cell.value, format_s).date()
                        row_dict['age'] = relativedelta(death_datetime, datetime.strptime(row_dict.get('date_birth'),
                                                                                          format_s).date()).years
                    elif type(cell.value) is datetime:
                        row_dict['death_date'] = cell.value.strftime(format_s)
                        row_dict['age'] = relativedelta(datetime.strptime(row_dict.get('death_date'), format_s),
                                                        datetime.strptime(row_dict.get('date_birth'), format_s)).years

                    else:
                        row_dict['death_date'] = None
                        row_dict['age'] = relativedelta(datetime.today(),
                                                        datetime.strptime(row_dict.get('date_birth'), format_s)).years
                else:
                    row_dict['gender'] = 'чоловік' if cell.value in ['m', 'ч'] else 'жінка'
            search_list.append(row_dict)

        counter = 0
        for sub in search_list:
            if s_string in sub['name'].lower():
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

    def save_person(self, person_work_book):
        s_per = [self.name, self.patronymic, self.surname, self.birth_date, self.death_date, self.gender]
        if self.per_sh.cell(1, 1).value is None:
            max_row_c = 1
        else:
            max_row_c = self.per_sh.max_row+1
        max_col_c = 7
        for i in range(1, max_col_c):
            cell_c = self.per_sh.cell(row=max_row_c, column=i)
            cell_c.value = s_per[i - 1]

        person_work_book.save('./diplom.xlsx')
        person_work_book.close()


class Gender_exception(Exception):
    def __init__(self, message='only two gender available'):
        super().__init__(message)