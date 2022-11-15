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
                view.show_contact_menu()
                choise_show_contact_menu = view.get_input("Выберите позицию: ")
                
                runing_choise_show_contact = True
                while runing_choise_show_contact:
                    match choise_show_contact_menu:
                        case '1':
                            id_contact = view.get_input("Введите id контакта: ")
                            
                            view.contact_data_entry_menu()
                            choise_contact_data_entry_menu = view.get_input("Выберите позицию: ")
                            
                            match choise_contact_data_entry_menu:
                                case '1':
                                    model.change_field("name")
                                case '2':
                                    model.change_field("surname")
                                case '3':
                                    model.change_field("number")
                                case '4':
                                    model.change_field("number+")
                                case '5':
                                    model.funct_back("back")
                        # case '2':
                        # case '3':
                        
                # view.choise_contact() # Выбор контакта
                # view.find_contact()
            case '2':
                None
            case '3':
                None
            case '4':
                None
            case 'exit':
                running = False


