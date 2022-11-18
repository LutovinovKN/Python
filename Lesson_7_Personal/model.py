import json
from pprint import pprint


def get_contact():
    contact = {}    # Создаём словарь
    # Назначаем поля
    fields = [
            ('name', 'имя'), ('surname', 'фамилию'), ('phones', 'телефон'),
            ('b-day', 'день рождения'), ('work', 'место работы')
            ]

    for field in fields:    # Перебираем каждое поле в списке "поля", начиная с нулевого ключ = введите ключ
        contact[field[0]] = input(f'Введите {field[1]}: ').capitalize()

    additional_phone = input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

    while additional_phone: # Пока вписываем дополнительные номера, добавляем к уже существующим
        contact['phones'] += ';' + additional_phone
        additional_phone = input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

    # print(contact)
    try:    # Метод исключения, в файл записывается только список 
        with open('contacts.json', 'r') as file: # Открываем и читаем contacts.json
            contacts = json.load(file)
    except Exception:
        contacts = []

    contacts.append(contact) # Добавляем контакт в список контактов

    with open('contacts.json', 'w') as file: # Записывает в contacts.json или создаём его если нет
        json.dump(contacts, file, indent=2, ensure_ascii=False)

    # print(contacts)


def get_all_contact():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
            text = json.load(f) #загнали все из файла в переменную
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
    except Exception:
        print('Список пуст')
        


def get_del_contact():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
            text = json.load(f) #загнали все из файла в переменную
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
        id_contact = int(input("Введите id контакта, который хотите удалить: "))
        for count, i in enumerate(text, start=1):
            if count == id_contact:
                text.pop(count - 1)
        with open('contacts.json', 'w') as file: # Записывает в contacts.json или создаём его если нет
                    json.dump(text, file, indent=2, ensure_ascii=False)
    except Exception:
            print('Список пуст')





