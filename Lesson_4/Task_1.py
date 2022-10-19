# Вычислить число Пи c заданной точностью d
#*   Пример:
#!      3.141592653589793
#?   при d = 0.001, π = 3.141
#?   при d = 0.1, π = 3.1
#?   при d = 0.00001, π = 3.14154
#?   d от 0.1 до 0.0000000001
# !!! не округлять константу math
from decimal import Decimal
from math import *
from unicodedata import decimal
# d = input('Введите число в пределах от 0.1 до 0.0000000001: ')
while True:
        try:
            d = abs(Decimal(input('Введите число в пределах от 0.1 до 0.0000000001: ')))
            break 
        except ValueError:
            print("Not an float number!")
            continue

num_pi = asin(sqrt(1 - 1**2))+ abs(asin(1)) * 2
print(num_pi)
if num_pi == pi:
    print("Число Пи найдено верно!")
else:
    print("Число Пи найдено неверно!")
print(round(num_pi, len(str(d))-2))

