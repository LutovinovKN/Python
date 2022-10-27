#    Создайте программу для игры с конфетами человек против человека.
#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""

from random import randint, uniform, random, choice
greeting = ('''Здравствуйте! Вас приветствует игра "Забери все конфеты!"
Основные правила игры:
1. нам будет дано 2021 конфета
2. за один ход мы можем взять не более 28 конфет'
3. победит тот, кто заберёт последнюю конфету
Итак, начнём!''')

messages = ['Ваша очередь брать конфеты:', 'Ваш ход:', 'Возьмите конфеты, но не жадничайте', 
            'Сколько конфет возьмёте?', 'Берите конфеты', 'А вы ненасытный! Так и попа слипнется! берите конфеты']
print(greeting)

def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'ЖралБот'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]

def get_rules(players):
    count_candy = int(input('\nСколько конфет будем разыгрывать?\n '))
    quantity = int(input('\nСколько максимально будем брать конфет за один ход?\n '))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [count_candy, quantity, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    # print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'        # окончание слов
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'        # окончание слов
    else:
        letter = ''         # окончание слов
    while rules[0] > 0:
        if not count % 2:
            if 0 < rules[0] < rules[1]:
                move = rules[0] % rules[1]
            else:
                move = rules[0] % rules[1] + 1
            print(f'Я возьму {move}\n')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            # сделаем количество попыток неверного ввода, чтобы игра не была бесконечной
            if move > rules[0] or move > rules[1]:
                print(f'Жадина! это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас осталось {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print('Очень жаль, у Вас не осталось попыток. Game over!')
        
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}\n')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

print(greeting)

players = introduce_players()       # Приветствие
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')