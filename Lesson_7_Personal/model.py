import json

contact = {}

fields = [('name', 'имя'), ('surname', 'фамилию'), ('phones', 'телефон')]

for field in fields:
    contact[field[0]] = input(f'Введите {field[1]}: ')

additional_phone = input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

while additional_phone:
    contact['phones'] += ';' + additional_phone
    additional_phone = input('Введите дополнительный телефон (пустой ввод, чтобы отказаться): ')

print(contact)

with open('contacts.json', 'w', encoding='UTF8') as file:
    json.dump(contact, file)

with open('contacts.json', 'r', encoding='UTF8') as file:
    data = json.load(file)

print(data)





