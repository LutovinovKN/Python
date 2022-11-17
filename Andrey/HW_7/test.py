import csv
from tabulate import tabulate


def get_phonebook() -> list:
    try:
        with open('contacts.csv', 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            contacts = sorted([row for row in reader], key=lambda x: x[1]+x[2]+x[0])
            return contacts
    except FileNotFoundError:
        with open('contacts.csv', 'a', encoding='UTF8') as f:
            pass
        return []


def show_book(book: dict) -> None:
    if not book:
        print('Список контактов пуст')
    else:
        for contact in book:
            contact[-1] = contact[-1].replace(';', '\n')
        headers = ['id', 'Имя', 'Фамилия', 'Дата рождения', 'Место работы', 'Телефоны']
        print(tabulate(book, headers=headers, tablefmt='fancy_grid'))


phonebook = get_phonebook()
show_book(phonebook)


def get_contact():
    name = input('Введите имя: ')
    while not name:
        name = input('Имя обязательно для ввода: ')
    surname = birthdate = employer = '-'
    surname = input('Введите фамилию: ')
    birthdate = input('Введите дату рождения: ')
    employer = input('Место работы: ')
    more_phones = True
    phones = input('Введите телефон: ')
    while not phones:
        phones = input('Введите хотя бы один номер телефона: ')
    while more_phones:
        reply = input('Хотите ввести еще один номер? ("д", если да, любой другой символ, если нет): ')
        if reply.lower() == 'д':
            another_number = input('Введите номер: ')
            while not another_number:
                another_number = input('Вы ничего не ввели. Введите еще один номер или введите "н" для выхода: ')
                if another_number == 'н':
                    break
                elif another_number:
                    phones += '; ' + another_number
        else:
            more_phones = False
    return name, surname, birthdate, employer, phones