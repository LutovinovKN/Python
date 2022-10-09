#   Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти:')
number = int(input())
if number == 1:
    print("X > 0, Y > 0")
elif number == 2:
    print("X > 0, Y < 0")
elif number == 3:
    print("X < 0, Y < 0")
elif number == 4:
    print("X < 0, Y > 0")
elif number > 4 or number < 1:
    print("Учите математику, в 2-х мерной системе всего 4 четверти от 1 до 4")