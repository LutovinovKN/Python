def show_info(input_value):
    print(input_value)


def get_input(output_value):
    return input(output_value) #.lower()


def menu():
    print(  '''\nГлавное меню:
            1 - Открыть список контактов
            2 - Добавить контакт
            3 - Удалить контакт
            exit - Выход'''
        )

def contact_list():
    print("Список контактов:")


def show_change_and_search_menu():
    print(
            '''
            Выберите позицию:
            1 - Изменить контакт
            2 - Поиск контакта
            back - Назад
            '''
        )


def show_chenge_contact():
    print(
            '''
            1 - Изменить имя
            2 - Изменить фамилию
            3 - Изменить номер телефона
            4 - Изменить день рождения
            5 - Изменить место работы
            6 - Изменить/добавить университет
            7 - Изменить/добавить школу
            back - Назад
            '''
        )