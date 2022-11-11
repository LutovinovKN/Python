import model
import view

def start():

    view.showinfo("hello! welcome to calculator!")

    
    a = view.getNumb("input int value --> ")
    choice = view.getNumb("выбери действие: '+', '-', '*', '/': ")
    b = view.getNumb("input int value --> ")
    model.init(a,b)
    
    match choice:
        case '+':
            result = model.summa()
        case '-':
            result = model.diff()
        case '*':
            result = model.mult()
        case '/':
            result = model.div()
            


    # result = model.enter()

    view.showinfo(result)
