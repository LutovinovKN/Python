# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

#   Пример двух заданных многочленов:
#?  23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#?  17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

#   Результат:
#?  40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0 40x9

# with open(r'/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_1.txt', "r") as file:
#     for line in file:
#         print(line)
# with open(r'/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_2.txt', "r") as file:
#     for line in file:
#         print(line)

#?  Индексы unicod
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

path = '/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_1.txt'
f = open(path, "r")
equation_5_1 = f.read()
print(equation_5_1)
f.close()
path = '/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_2.txt'
f = open(path, "r")
equation_5_2 = f.read()
print(equation_5_2)
f.close()

print()

#?  убираем пробелы, а также "= 0"
#?  находим отрицательные элементы через "-" и заменяем на "+-"
#?  разбиваем по "+" строку и вносим данные в элементы списка
def split_list(n_equation):
    tmp = n_equation.replace(" ", "")[:-2]
    result = tmp.replace("-", "+-").split("+")
    print(result)       #! перед отправкой не забыть закомментировать
    return result

new_equation_5_1 = split_list(equation_5_1) #!  Удалить перед отправкой
new_equation_5_2 = split_list(equation_5_2) #!  Удалить перед отправкой

def tuple_equation(n_equation):
    equation = {}
    equation_tuple = []
    for i in range(len(n_equation)):
        
        equation_tuple.append(n_equation[i].partition('x'))
        
        
    print(equation_tuple)       #! перед отправкой не забыть закомментировать
    return equation_tuple

tuple_of_equation1 = tuple_equation(new_equation_5_1)
tuple_of_equation2 = tuple_equation(new_equation_5_2)




# ________________________________________________________________________________________________________-


# import re
# import itertools


# file1 = '33_Polynomial.txt'
# file2 = '33_Polynomial2.txt'
# file_sum = '34_Sum_polynomials.txt'

# # Получение данных из файла

# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# # Получение списка кортежей каждого (<коэффициент>, <степень>)

# def convert_pol(pol):
#     pol = pol.replace('= 0', '') # пропуск = 0 и пробелов
#     pol = re.sub("[*|^| ]", " ", pol).split('+') # ставит пробел на место [*|^| ] в переменной pol и разделяет плюсами
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)  # Вставляет 1 на индекс 0
#         if i[-1] == 'x': i.append(1)    # добавляет в конец 1
#         if len(i) == 1: i.append(0)     # добавляет в конец 0
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol] # превращаем в кортеж
#     return pol

# # Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# # Составление итогового многочлена

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)