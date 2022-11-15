def show_info(input_value):
    print(input_value)


def get_input(output_value):
    return input(output_value).lower()


def menu():
    print(  '''Главное меню:
            1 - Открыть список контактов
            2 - Добавить контакт
            3 - Удалить весь список контактов
            4 - Закрыть телефонный справочник
            exit - Выход'''
        )

def show_contact_list():
    None
#     choise_contact_list = view.contact("выберите позицию")
    
#     match choise_contact_list:
#         case '1':
#             view.contact()
#         case '2':
#             view.contact_find()
#         case '3':
#             view.back()

def show_contact_menu():
    print('''Список контактов
            1 - Выбрать контакт
            2 - Поиск контакта
            back - Назад'''
        )


# def contact():
#     print(  '\n{name_contact}\n'
#             '1. Изменить контакт'
#             '2. Удалить контакт'
#             '3. Назад'
#         )


def contact_data_entry_menu():
    print('''Корректировка контакта{name_contact}
            1 - Добавить имя
            2 - Добавить фамилию
            3 - Добавить номер телефона
            4 - Добавить рабочий номер телефона
            back - Назад'''
        )


# def contact_find():
#     print('\nПоиск контакта\n'
#             '1. Введите имя'
#         )