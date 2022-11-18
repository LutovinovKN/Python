import csv

column_names = ['name', 'surname', 'birthdate', 'employer', 'phones']

def get_phonebook() -> list:
    try:
        with open('phonebook.csv', 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            return sorted(list(reader), key=lambda x: (x[1] + x[2] + x[3]).lower())
    except FileNotFoundError:
        return []

def get_contact() -> dict:
    name = input('Введите имя: ')
    while not name:
        name = input('Имя обязательно для ввода: ')
    surname = input('Введите фамилию: ')
    birthdate = input('Введите дату рождения: ')
    work = input('Введите место работы: ')
    more_phones = True
    phones = input('Введите телефон: ')
    while not phones:
        phones = input('Введите хотя бы один номер телефона: ')
    while more_phones:
        reply = input('Введите еще один номер (для выхода введите "н"): ')
        while not reply:
            reply = input('Вы ничего не ввели. Введите номер телефона (для выхода введите "н"): ')
        if reply.lower() == 'н':
            more_phones = False
        else:
            phones += f';{reply}'
    columns = [name, surname, birthdate, work, phones]
    contact = {}
    for i in range(len(columns)):
        contact[column_names[i]] = columns[i] if columns[i] else '-'
    return contact

