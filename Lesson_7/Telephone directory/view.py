def showinfo(input_value):
    print(input_value)


def getNumb(output_value):
    return input(output_value) 


def showMenu():
    print('\nГлавное меню:\n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать все контакты\n'
          '4. Поиск контакта\n'
          '5. Добавить контакт\n'
          '6. Изменить контакт\n'
          '7. Удалить контакт\n'
          '0. Выход')


def inputInt(text):
      while True:
            try:
                  number = int(input(text))
                  return number
            except:
                  print('Ошибка! Введите целое число!')