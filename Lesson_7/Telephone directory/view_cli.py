from sqlalchemy.ext.asyncio import session
import view

class CLI_PhoneBook():

    # __init__():

        # id = session.query(.store_onoff).filter_by(store_url=app.config['SITE']).first()

        # id = id
        # first_name
        # last_name
        # patronymic
        # birthday
        # phone_person
        # phone_work
        # email
        # group
        # city_id

    # def getUseTypeDB(self):
    #
    #     return self.
    def menu_main(self):
        view.inputInt(f'Выберите действие:\n'
                      f'1 - Отобразить все данные\n'
                      f'2 - Найти запись в справочнике\n'
                      f'3 - Добавить запись\n'
                      f'4 - экспортировать в ...'
                      f'0 - ВЕРНУТЬСЯ НАЗАД\n')

    def menu_person(self):
        view.inputInt(f'Выберите действие:\n'
                      f'1 - Изменить поле:\n'
                      f'2 - Удалить запись'
                      f'0 - ВЕРНУТЬСЯ НАЗАД\n')

    def menu_edit_field(self):
        view.inputInt(f'Выберите действие:\n'
                      f'1 - Имя\n'
                      f'2 - Фамилия\n'
                      f'3 - Отчество\n'
                      f'4 - Дату рождения\n'
                      f'5 - Номер мобильного телефона\n'
                      f'6 - Номер рабочего телефона\n'
                      f'7 - Электронную почту\n'
                      f'8 - Группу контакта\n'
                      f'9 - Город\n'
                      f'0 - ВЕРНУТЬСЯ НАЗАД\n')

    def menu_edit_group_field(self):
        view.inputInt(f'Выберите группу из списка:\n'
                      f'1 - Семья\n'
                      f'2 - Работа\n'
                      f'3 - Друзья\n'
                      f'0 - ВЕРНУТЬСЯ НАЗАД\n')

    def menu_export(self):
        view.inputInt(f'Выберите действие:\n'
                      f'1 - в SCV\n'
                      f'2 - в JSON\n'
                      f'3 - в SQLite\n'
                      f'0 - ВЕРНУТЬСЯ НАЗАД\n')


