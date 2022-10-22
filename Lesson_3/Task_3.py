#     Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*      Пример:
#*      [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from math import *

num_list = []
for i in range(5):
    # num = float(input("Введите вещественное число: "))
    while True:
        try:
            num = float(input("Введите вещественное число: "))
        except ValueError:
            print("Not an float number!")
            continue
        else:
            print("Yes an float number!")
            break 
    if (round(num - int(num), 2)) == 0:
        continue
    num_list.append(round(num - int(num), 2))
print(num_list)
print(f'Разница между максимальной и минимальной дробной частью равна: {round(max(num_list) - min(num_list), 2)}')
