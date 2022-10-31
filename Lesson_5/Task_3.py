# Инициализация карты
field = [1,2,3,
        4,5,6,
        7,8,9]

# Инициализация победных линий
victories = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

# Вывод карты на экран
def print_field():
    print("-------------")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")

# Сделать ход в ячейку
def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol



# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"   

    return win

# поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O,sum_X):

    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(3):
            if field[line[j]] == "O":
                o = o + 1
            if field[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(3):
                if field[line[j]] not in ["O", "X"]:
                    step = field[line[j]]
    return step

# выбор хода бота
def bot():        

    step = ""

    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2,0)

    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0,2)        

    # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1,0)           

    # 4) центр пуст, то занимаем центр
    if step == "" and field[4] not in ["X", "O"]:
            step = 5           

    # 5) если центр занят, то занимаем первую ячейку
    if step == "" and field[0] not in ["X", "O"]:
            step = 1           

    return step

# Основная программа
# sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
game_over = False
human = True
player = input('Давайте познакомися. Как Вас зовут?\n')
while not game_over:
    # 1. Показываем карту
    print_field()

    # 2. Спросим у играющего куда делать ход
    if human == True:
        valid = False
        while not valid:
            symbol = "X"
            step = int(input(f"{player}, ваш ход: "))
            try:
                step = int(step)
            except:
                print ("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= step <= 9:
                if (str(field[step-1]) not in "XO"):
                    field[step-1] = step
                    valid = True
                else:
                    print ("Эта клетка уже занята, попробуйте ввести число ещё раз")
            else:
                print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

    else:
        print("21-Bot делает ход: ")
        symbol = "O"
        step = bot()

    # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
    if step != "":
        step_field(step,symbol) # делаем ход в указанную ячейку
        win = get_result() # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "Ничья!"
    human = not(human)
    
print_field()

if win == "O":
    win = "21-Bot"
    print("Победил", win)
elif win == "Ничья!":
    print("Ничья!")
else:
    win = player
    print("Победил", win)
# Игра окончена. Покажем карту. Объявим победителя.        
