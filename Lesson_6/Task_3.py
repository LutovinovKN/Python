#     Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*     Пример:
#*      [2, 3, 4, 5, 6] => [12, 15, 16];
#*      [2, 3, 5, 6] => [12, 15]

from random import randint
from math import *
while True:
    try:
        n = int(input('How long is the list you need? Enter a number: '))       
    except ValueError:
        print("Not an integer number!")
        continue
    else:
        print("Yes an integer number!")
        break 
tmp = 0
numbers = []
for i in range(n):
    tmp = randint(-9, 9)
    numbers.append(tmp)
print(numbers)

composition_num = list(map(lambda i: numbers[i] * numbers[-(i+1)], range(ceil(n/2))))

# версия 2
# def composition(i):
#     return numbers[i] * numbers[-(i+1)]
# composition_num = list(map(composition, range(ceil(n/2))))

# версия 3
# def composition(numbers):
#     half_list = ceil(n / 2)
#     return [numbers[i] * numbers[-(i+1)] for i in range(half_list)]
# composition_num = list(composition(numbers))

# Версия 4
# composition_num = []
# half_list = ceil(n / 2)
# for i in range(half_list):
#     composition_num.append(numbers[i] * numbers[-(i+1)])
    
print("Произведением пар чисел списка numbers, является следующий список: ", composition_num)