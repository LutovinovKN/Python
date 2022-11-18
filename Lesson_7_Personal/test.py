import json
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