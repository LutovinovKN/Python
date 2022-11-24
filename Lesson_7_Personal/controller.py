import model
import view


def run():
    
    view.show_info("Вы находитесь в главном меню телефонного справочника")
    running = True
    while running:
        view.menu()
        choise_menu = view.get_input("Выберите позицию: ")
        print()
        match choise_menu:
            case '1':
                all_contacts = model.get_all_contact()
                view.show_change_and_search_menu() #? Показывает меню изменения и поиска контакта
                running_change_and_found = True
                while running_change_and_found:
                    choise_menu = view.get_input("Выберите позицию: ")
                    print()
                    match choise_menu:
                        case "1":
                            chenge_contact = model.get_chenge_contact(all_contacts)
                            running_chenge_contact = True
                            while running_chenge_contact:
                                view.show_chenge_contact() #? Показывает меню изменения контакта и добавления новых колонок
                                print()
                                choise_menu = view.get_input("Выберите позицию: ")
                                match choise_menu:
                                    case '1':
                                        model.get_update_name(chenge_contact)
                                    case '2':
                                        model.get_update_surname(chenge_contact)
                                    case '3':
                                        model.get_update_phone(chenge_contact)
                                    case '4':
                                        model.get_update_bday(chenge_contact)
                                    case '4':
                                        model.get_update_work(chenge_contact)
                                    case '5':
                                        model.get_update_university(chenge_contact)
                                    case '6':
                                        model.get_update_school(chenge_contact)
                                    case 'back':
                                        running_chenge_contact = False
                                model.save(all_contacts)
                        case "2":
                            find_contact = model.get_find_contact()
                        case "back":
                            running_change_and_found = False
            case '2':
                contact = model.get_new_contact()
            case '3':
                del_contact = model.get_del_contact()
            case 'exit':
                running = False


