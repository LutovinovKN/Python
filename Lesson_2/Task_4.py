# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

from random import randint

n = int(input('Введите число n: '))
tmp = 0
numbers = []
for i in range(n):
    # *     Исключаем из рандома 0
    while True:
        tmp = randint(-n, n)
        if tmp != 0: break
    numbers.append(tmp)
print(numbers)

posit = []
enter_posit = int(input(f"Введите, сколько позиций от 0 до {n} вы хотите выбрать? "))
for i in range(enter_posit):
    if enter_posit == 0:
        break
    posit.append(int(input("Ввведите позицию: ")))
print(posit)
composition_posit = 1
for i in range(enter_posit):
    composition_posit *= numbers[posit[i]]
print(composition_posit)