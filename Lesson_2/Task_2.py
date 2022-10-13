# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

#*  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

while True:
    try:
        n = int(input("Enter number n: "))       
    except ValueError:
        print("Not an integer!")
        continue
    else:
        print("Yes an integer!")
        break 

list_n = []
total = 1
for i in range(1, n + 1):
    total *= i
    list_n.append(total)
print(list_n)