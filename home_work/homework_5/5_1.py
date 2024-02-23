

a = []
exit_var = ['Y', 'y', 'Д', 'д']
while a not in exit_var:

    raw_string = input('Введіть ім\'я та вік: ')
    try:
        name, age = raw_string.split()
    except ValueError:
        name = ''
        age = ''

    template0 = 'Помилка, повторіть введення'
    template1 = f'Привіт, шкет {name}'
    template2 = f'Як справи, {name}?'
    template3 = f'Що бажаєте, {name}?'
    template4 = f'{name}, ви брешете - у наш час стільки не живуть..'

    if not age.isdigit() or int(age) <= 0:
        print(template0)
        continue
    elif int(age) < 10:
        print(template1)
    elif int(age) <= 18:
        print(template2)
    elif int(age) < 100:
        print(template3)
    else:
        print(template4)

    choice = input('Бажаєте вийти? (Д/Y)')
    # a = 0 if 'Y' in choice.upper() else 0 if 'Д' in choice.upper() else 1
    a = choice
