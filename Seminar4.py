# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# str_num = "4 6 8 4 3 2 0 5 8 88 -2 hello -9".split()
# a = []

# for i in str_num:
#     try:
#         a.append(int(i))  
#     except ValueError:
#         print("Not an integer number!")
#         continue

# print(a)   
# print(min(a), max(a))




# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
function = open("primer.md","r")
print(*function)

import math 
print("Введите коэффициенты для уравнения") 
print("ax^2 + bx + c = 0:") 
a = float(input("a = ")) 
b = float(input("b = ")) 
c = float(input("c = ")) 
discr = b ** 2 - 4 * a * c 
print("Дискриминант D = %.2f" % discr) 
if discr > 0: 
    x1 = (-b + math.sqrt(discr)) / (2 * a) 
    x2 = (-b - math.sqrt(discr)) / (2 * a) 
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2)) 
elif discr == 0: 
    x = -b / (2 * a) 
    print("x = %.2f" % x) 
else: print("Корней нет") 

# with open("primer.md","r") as function: 
#     function.write('line 1\n')
#     print(function)

# с помощью математических формул нахождения корней квадратного уравнения

# вводим из файла


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. 