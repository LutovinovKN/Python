#     Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*     Пример:
#*      45 -> 101101
#*      3 -> 11
#*      2 -> 10

def inputNumber(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print("Вы не ввели число, попробуйте снова!")
            break

numb = inputNumber(msg = "Пожалуйста, введите целое число: ")

res = ''

while numb:
    res = str(numb % 2) + res
    numb = numb // 2

print(res if res else '0')