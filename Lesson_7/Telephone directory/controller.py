import model
import view

def start():
    while True:
        view.showMenu()
        choice = view.inputInt('Выберите пункт меню: ')
        match (choice):
            case 1:
                try:
                    openFile()
                    print('\nКнига загружена!')
                except:
                    print('Ошибка работы с файлом')
            case 2:
                try:
                    saveFile()
                    print('\nКнига сохранена!')
                except:
                    print('Ошибка работы с файлом')
            case 3:
                showAll()
            case 4:
                findContact()
            case 5:
                addContact()
            case 6:
                changeContact()
            case 7:
                deleteContact()
            case _:
                return False

def openFile():
    pass

def saveFile():
    pass

def showAll():
    pass
def findContact():
    pass
def addContact():
    pass

def changeContact():
    pass

def deleteContact():
    pass
    
