# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Записываем результат в файл.

#    Пример:
#?   k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#?   k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint, uniform, random, choice, sample
# индексы unicode
indexes = { 0: "\u2070",
            1: "\u00B9",
            2: "\u00B2",
            3: "\u00B3",
            4: "\u2074",
            5: "\u2075",
            6: "\u2076",
            7: "\u2077",
            8: "\u2078",
            9: "\u2079"
        }

n = input("Введите число необходимой степени дискриминанта: ")
equation = []

for i in range(int(n), 0, -1):
    lst = [indexes[int(j)] for j in str(i)]
    degree = ''.join(lst)
    a = randint(0, 100)
    test = ['+', '-']
    rnd_sign = choice(test)
    
    if a == 0:
        continue
    elif a == 1:
        equation.append("X" + degree)
        equation.append('' + rnd_sign + '')
    else:
        if i == 1:
            equation.append(str(a) + "X")
            equation.append('' + rnd_sign + '')
        else:
            equation.append(str(a) + "X" + degree)
            equation.append('' + rnd_sign + '')

a = randint(0, 100)
if a == 0:
        equation.pop(-1)
else:
    equation.append(str(a))
res =' '.join(equation)
print(*"y = ", res)
with open("res_task_4.txt", "w") as file:
    file.write(res)