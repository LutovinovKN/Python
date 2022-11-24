import json
import view

#? ####################################
def get_new_contact():
    contact = {}    # Создаём словарь
    # Назначаем поля
    fields = [
            ('name', 'имя'), ('surname', 'фамилию'), ('phones', 'телефон'),
            ('b-day', 'день рождения'), ('work', 'место работы')
            ]

    for field in fields:    # Перебираем каждое поле в списке "поля", начиная с нулевого ключ = введите ключ
        contact[field[0]] = view.get_input(f'Введите {field[1]}: ') #.capitalize()

    additional_phone = view.get_input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

    while additional_phone: # Пока вписываем дополнительные номера, добавляем к уже существующим
        contact['phones'] += ';' + additional_phone
        additional_phone = view.get_input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

    try:    # Метод исключения, в файл записывается только список 
        with open('contacts.json', 'r') as file: # Открываем и читаем contacts.json
            contacts = json.load(file)
    except Exception:
        print('Список отсутствует')
        contacts = []

    contacts.append(contact) # Добавляем контакт в список контактов

    with open('contacts.json', 'w') as file: # Записывает в contacts.json или создаём его если нет
        json.dump(contacts, file, indent=2, ensure_ascii=False)


#? ####################################
def get_all_contact():
    view.contact_list()
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
            text = json.load(f) #загнали все из файла в переменную
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            # count_symbols = max(len(i.values))
            # print('%-7s %5d %8.1f' % ('First', 483, 1.1)) 
            print(count, '\t|'.join(list(i.values())))
        return text
    except Exception as erorr:
        print('Список отсутствует')
        print(erorr.args[0])
        return []


#? ####################################
def get_del_contact():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
            text = json.load(f) #загнали все из файла в переменную
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
        id_contact = int(view.get_input("Введите id контакта, который хотите удалить: "))
        for count, i in enumerate(text, start=1):
            if count == id_contact:
                text.pop(count - 1)
        with open('contacts.json', 'w') as file: # Записывает в contacts.json или создаём его если нет
                    json.dump(text, file, indent=2, ensure_ascii=False)
    except Exception:
            print('Список отсутствует')


#? ####################################
def get_find_contact():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
            text = json.load(f) #загнали все из файла в переменную
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
        find_word = view.get_input("введите имя или фамилию контакта: ")
        print()
        result = [z for z in text if z["name"] == find_word or z["surname"] == find_word]
        for count, i in enumerate(result, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
        if not result:
            print(f"В справочнике нет контакта {find_word}")
        # else:
        #     print(result)
    except Exception:
            print('Данный id отсутствует')


#? ####################################
def get_chenge_contact(text):
    try:
        for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
            print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work'])
        id_contact = int(view.get_input("Введите id контакта, который хотите изменить: "))
        if len(text) > id_contact > 0:
            chenge_contact = text[id_contact - 1] #! Это изменить под коректировку контакта
            return chenge_contact
        print('Введите корректный контакт')
    except Exception:
            print('Список отсутствует')


#? ####################################
def get_update_name(id_contact):
    id_contact.update({'name': view.get_input("Введите имя: ")})

def get_update_surname(id_contact):
    id_contact.update({'surname': view.get_input("Введите фамилию: ")})

def get_update_phone(id_contact):
    id_contact.update({'phone': view.get_input("Введите номер телефона: ")})

def get_update_bday(id_contact):
    id_contact.update({'b-day': view.get_input("Введите дату рождения: ")})

def get_update_work(id_contact):
    id_contact.update({'work': view.get_input("Введите место работы: ")})

def get_update_university(id_contact):
    id_contact.update({'university': view.get_input("Введите университет: ")})

def get_update_school(id_contact):
    id_contact.update({'school': view.get_input("Введите школу: ")})


def open_file():
    with open('contacts.json', 'r', encoding='utf-8') as f: #открыли файл
        return json.load(f) 
            
            
def save(text):
    with open('contacts.json', 'w') as file: # Записывает в contacts.json или создаём его если нет
        json.dump(text, file, indent=2, ensure_ascii=False)