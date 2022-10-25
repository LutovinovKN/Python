# Вычислить число Пи c заданной точностью d
#*   Пример:
#!      3.141592653589793
#?   при d = 0.001, π = 3.141
#?   при d = 0.1, π = 3.1
#?   при d = 0.00001, π = 3.14154
#?   d от 0.1 до 0.0000000001
# !!! не округлять константу math
import math
from decimal import Decimal
from decimal import getcontext

def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
        Decimal(2)/(8*k+4) - 
        Decimal(1)/(8*k+5) -
        Decimal(1)/(8*k+6)) for k in range (precision))
print(pi(int(input('Введите число, сколько цифр числа Пи вам необходимо найти (Например: 2 => 3.1): '))))
print(math.pi)
