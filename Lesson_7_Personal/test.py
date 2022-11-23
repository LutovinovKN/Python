import view

text = [
    {
    "name": "Константин",
    "surname": "Лутовинов",
    "phones": "89515063050",
    "b-day": "14.07.1991",
    "work": "Рниирс"
    },
    {
    "name": "Елена",
    "surname": "Лутовинова",
    "phones": "89516034582",
    "b-day": "28.11.1991",
    "work": "1forma"
    },
    {
    "name": "Иван",
    "surname": "Иванов",
    "phones": "89516088582",
    "b-day": "28.11.1991",
    "work": "1forma"
    },
    {
    "name": "Иван",
    "surname": "Лутовинов",
    "phones": "89516034582",
    "b-day": "19.03.1989",
    "work": "1forma"
    }
]

def get_update_name(id_contact):
    id_contact.update({'name': view.get_input("Введите имя: ")})
def get_update_surname(id_contact):
    id_contact.update({'surname': view.get_input("Введите фамилию: ")})
def get_update_bday(id_contact):
    id_contact.update({'b-day': view.get_input("Введите дату рождения: ")})
def get_update_work(id_contact):
    id_contact.update({'work': view.get_input("Введите место работы: ")})
def get_update_university(id_contact):
    id_contact.update({'university': view.get_input("Введите университет: ")})
def get_update_school(id_contact):
    id_contact.update({'school': view.get_input("Введите школу: ")})


temporary_list = []
def displaying_lst_in_column(text):
    for count, i in enumerate(text, start=1): #создали цикл, который будет работать построчно
                print(count, i['name'], '\t|', i['surname'], '\t|', i['phones'], '\t|', i['b-day'], '\t|', i['work']) #! Из этого for нужно сделать функцию
displaying_lst_in_column(text)
id_contact = int(view.get_input("Введите id контакта, который хотите изменить: "))
for count, i in enumerate(text, start=1):
    if count == id_contact:
        get_update_name(text[count - 1])
        # print(text[count - 1])
        # text[count - 1].update({"name": view.get_input("Введите имя: ")})
        # temporary_list = text(count - 1)
        # get_update_name(temporary_list)
# print(temporary_list)
displaying_lst_in_column(text)
