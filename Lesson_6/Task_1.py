# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
#*  6782 -> 23
#*  0,56 -> 11
from functools import reduce

def list_num(number):
    new_list = []
    for i in range(len(str(number))):
        new_list.append(int(number) % 10)
        number = int(number) // 10
    return new_list

number = float(input("Введите число: "))
number *= (10 ** len(str(number)))

summa = reduce((lambda x, y: x + y), list_num(number))
print(summa)

