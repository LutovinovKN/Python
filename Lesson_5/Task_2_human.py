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

def get_rules(players):
    count_candy = int(input('\nСколько конфет будем разыгрывать?\n '))
    quantity = int(input('\nСколько максимально будем брать конфет за один ход?\n '))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first == 1:
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
        print(f'{players[count%2]}, {choice(messages)}')
        move = int(input())
        if move > rules[0] or move > rules[1]:
            print(f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if rules[0] >= move <= rules[1]:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0: print(f'Осталось {rules[0]} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
players = [player1, player2]

rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')