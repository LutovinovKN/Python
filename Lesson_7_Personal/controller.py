import model
import view


def run():
    
    view.show_info("Вы находитесь в главном меню телефонного справочника")
    running = True
    while running:
        view.menu()
        choise_menu = view.get_input("Выберите позицию: ")
        
        match choise_menu:
            case '1':
                view.show_contact_list() # Показыает список контактов
                runing_choise_show_contact = True
                while runing_choise_show_contact:
                    view.show_contact_menu()
                    choise_show_contact_menu = view.get_input("Выберите позицию: ")
                    match choise_show_contact_menu:
                        case '1':
                            id_contact = view.get_input("Введите id контакта: ")
                            
                            view.contact_data_entry_menu()
                            choise_contact_data_entry_menu = view.get_input("Выберите позицию: ")
                        case 'back':
                            runing_choise_show_contact = False
                            match choise_contact_data_entry_menu:
                                case '1':
                                    model.change_field("name")
                                case '2':
                                    model.change_field("surname")
                                case '3':
                                    model.change_field("number")
                                case '4':
                                    model.change_field("number+")
                                case '9':
                                    model.del_contact
                                case 'back':
                                    runing_choise_show_contact = False
                        
                # view.choise_contact() # Выбор контакта
                # view.find_contact()
            case '2':
                view.contact_add_menu() # Показывает меню создания контакта
                runing_add_contact = True
                while runing_add_contact:
                    choise_add_contact = view.get_input("Выберите позицию: ")
                    
                    match choise_add_contact:
                        case '1':
                            model.change_field("name")
                        case '2':
                            model.change_field("surname")
                        case '3':
                            model.change_field("number")
                        case '4':
                            model.change_field("number_plus")
            case '3':
                None
            case 'exit':
                running = False

def get_contact() -> dict:
    name = input('Введите имя: ')
    while not name:
        name = input('Имя обязательно для ввода: ')
    surname = input('Введите фамилию: ')
    number = input('Введите телефон: ')
    while not numbers:
        numbers = input('Без номера телефона никак: ')
    while number_plus:
        reply = input('Введите еще один номер (для выхода введите "н"): ')
        while not reply:
            reply = input('Вы ничего не ввели. Введите номер телефона (для выхода введите "н"): ')
        if reply.lower() == 'н':
            number_plus = False
        else:
            number_plus += f';{reply}'
    columns = [name, surname, number, number_plus]
    contact = {}
    
