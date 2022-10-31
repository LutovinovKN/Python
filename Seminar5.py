import os
import random
import time

candy_start = 2021
candy_min = 1
candy_max = 28
candy_count = 0
boot_sleep = 2


class msg():
    first = '1'
    second = '2'

class colors:
    '''Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

class ico:
    candy = '🍬'
    lollypop = '🍭'
    cake = '🍰'
    honey = '🍯'
    donut = '🍩'
    cookie = '🍪'
    chocolate = '🍫'
    win_bot = '🦾'
    win_user = '💪'
    ava_user = '👤'
    ava_robot = '🤖'
    ava_ai = '🔮'
    trophy = '🏆'
    warning = '⚠'

def nextPlayer(next_player):
    if next_player == 1:
        next_player = 2
    elif nextPlayer == 2:
        next_player = 1
    return next_player

def draw():
    print('ЖЕРЕБЬЁВКА!\nГенерируется случайное число "1 или 2".\n'
        '1й или 2й игрок соответственно получает право первого хода\n')
    player = random.randint(1, 2)
    time.sleep(2)
    print(f'---> {player}й <--- игрок получает право первого хода\n\n')
    time.sleep(1)
    return player

def interfaceGame(candy_count):
    os.system('cls')
    print((colors.reverse + " " + colors.reset) * 120 + '\n')
    candy_left = candy_start - candy_count
    print(
        # f'|||\t'
        f'Осталось конфет: {colors.reverse + " " + str(candy_left) + " " + colors.reset}'
        f'\t\t{ico.candy}\t\t'
        f'Взято конфет: {colors.reverse + " " + str(candy_count) + " " + colors.reset}'
        f'\t\t{ico.candy}\t\t'
        f'Всего конфет: {colors.reverse + " " + str(candy_start) + " " + colors.reset}'
        # f'\t\t|||'
    )
    print('\n' + (colors.reverse + " " + colors.reset) * 120 + '\n')

def candyLeft(candy_count: int) -> int:
    value = candy_start - candy_count
    return value

candyLeftValue = candyLeft(candy_count)

def inputNumber():
    try:
        number = int(input("Пожалуйста, введите число конфет: "))
        # candyLeftValue = candyLeft(candy_count)
        if 0 != 0:
            pass
        elif number <= candy_min - 1 or number >= candy_max + 1:
            print(f'Столько конфет "{number}" брать нельзя, возьмите в интервале от {candy_min} до {candy_max}')
            return inputNumber()
        elif candyLeftValue + 1 < candy_max + 1:
            if number <= candy_min - 1 or number >= candyLeftValue + 1:
                print(f'Столько конфет "{number}" брать нельзя, возьмите в интервале от {candy_min} до {candyLeftValue}')
                return inputNumber()
        return number
    except ValueError:
        print(f'Вы не ввели число, попробуйте снова! Возьмите {ico.candy}')
        return inputNumber()

def stepPlayer(last_player):
    print(f'DEF Ход игрока {last_player}')
    numb = inputNumber()
    print(f'Игрок {last_player} взял {numb}\n')
    return numb

def stepBot():
    print(f'Ход БОТА')
    # candyLeftValue = candyLeft(candy_count)
    max = candy_max + 1
    if candyLeftValue + 1 < candy_max + 1:
        if max <= candy_min - 1 or max >= candyLeftValue + 1:
            numb = int(random.randint(candy_min, candyLeftValue + 1))
    elif max <= candy_min - 1 or max >= candy_max + 1:
        numb = int(random.randint(candy_min, candy_max + 1))
    time.sleep(2)
    print(f'Бот взял {numb}')
    time.sleep(2)
    return numb

def blackBoxAi(last_player, PlayerNumb, maxNumb):
    if last_player == 2 and candy_count == 0:
        step_1 = int(candy_start % maxNumb)
        numb = step_1
    elif candyLeftValue >= candy_start - candy_count:
        if PlayerNumb == maxNumb:
            numb = candy_max
        else:
            step_2 = int(maxNumb - PlayerNumb)
            numb = step_2
    else:
        numb = maxNumb
    return numb

def stepBotAi(PlayerNumb):
    print(f'Ход БОТА AI')
    candyLeftValue = candyLeft(candy_count)
    max = candy_max + 1
    if candyLeftValue + 1 < candy_max + 1:
        if max <= candy_min - 1 or max >= candyLeftValue + 1:
            numb = blackBoxAi(last_player, PlayerNumb, candyLeftValue)
    elif max <= candy_min - 1 or max >= candy_max + 1:
        numb = blackBoxAi(last_player, PlayerNumb, candy_max)
    time.sleep(2)
    print(f'БОТ AI взял {numb}')
    time.sleep(2)
    return numb

def selectGame():
    interfaceGame(candy_count)
    game = int(input(f'Выбирете вариант игры:\n\t\t'
                            f'1 - {ico.ava_user}Человек против {ico.ava_user}человека\n\t\t'
                            f'2 - {ico.ava_user}Человек против {ico.ava_robot}бота\n\t\t'
                            f'3 - {ico.ava_user}Человек против {ico.ava_ai}Ai\n\n\t\t'
                    f'ВВЕДИТЕ ЧИСЛО ВАРИНАНТА ИГРЫ: '))
    if game == 1:
        game = 1
    elif game == 2:
        game = 2
    else:
        game = 3
    return game
select_game = selectGame()

draw_player = draw()
next_player = nextPlayer(draw_player)
candy_count = 0
# last_player = 2
PlayerNumb = 0
while True:
    if candy_start - candy_count == 0:
        print(f'{ico.trophy} ПОБЕДИЛ ИГРОК {last_player}'
            f'{ico.candy}{ico.cake}{ico.donut}{ico.chocolate}{ico.lollypop}')
        break
    else:
        interfaceGame(candy_count)
        # ход игрока 1
        if next_player == 1:
            last_player = 1
            numb = stepPlayer(last_player)
            next_player = 2
            PlayerNumb = numb
        # ход игрока 2
        elif next_player == 2:
            last_player = 2
            if select_game == 1:
                numb = stepPlayer(last_player)
            elif select_game == 2:
                numb = stepBot()
            else:
                numb = stepBotAi(PlayerNumb)
            next_player = 1

    candy_count += numb
