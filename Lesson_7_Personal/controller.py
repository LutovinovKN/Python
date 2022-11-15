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
                            model.change_field("number+")
            case '3':
                None
            case 'exit':
                running = False


