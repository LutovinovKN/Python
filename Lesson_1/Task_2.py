#     Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from tkinter import N


print("введите числа X, Y, Z:")
x, y, z = int(input()), int(input()), int(input())

print('Проверяем условие: \n ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n подставим значение')
print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
f1 = -(x or y or z)
f2 = -x and -y and -z
if f1 == f2:
    print("они равны")
else:
    print('они не равны')