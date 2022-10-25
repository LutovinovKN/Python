# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#*  Пример двух заданных многочленов:
#?  23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#?  17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#*  Результат:
#?  40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0 40x9
import numpy
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
unicode_in_int = {  "": "",
                    "⁰": "0",
                    "¹": "1",
                    "²": "2",
                    "³": "3",
                    "⁴": "4",
                    "⁵": "5",
                    "⁶": "6",
                    "⁷": "7",
                    "⁸": "8",
                    "⁹": "9"
                }

# path = '/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_1.txt'
# f = open(path, "r")
equation_5_1 = '23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0'
# print(equation_5_1)
# f.close()
# path = '/home/sideshow/GeekBrains/Семинар/Python/Lesson_4/equation_5_2.txt'
# f = open(path, "r")
equation_5_2 = '17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0'
# print(equation_5_2)
# f.close()

print()

#?  убираем пробелы, а также "= 0"
#?  находим отрицательные элементы через "-" и заменяем на "+-"
#?  разбиваем по "+" строку и вносим данные в элементы списка
def split_list(n_equation):
    tmp = n_equation.replace(" ", "")[:-2]
    result = tmp.replace("-", "+-").split("+")
    print(result)       #! перед отправкой не забыть закомментировать
    return result

new_equation_5_1 = split_list(equation_5_1) 
new_equation_5_2 = split_list(equation_5_2) 

def tuple_equation(n_equation): # разбиваем на элементы (-27х⁹ => ('-27', 'x', '⁹'))
    equation = {}
    equation_tuple = []
    for i in range(len(n_equation)):
        equation_tuple.append(n_equation[i].partition('x'))            
    print(equation_tuple)       #! перед отправкой не забыть закомментировать
    return equation_tuple
print()

#?  Находим максимальную степень
def max_degree(first_tuple, second_tuple):
    res1 = ''
    for i in first_tuple[0][-1]:
        if i in unicode_in_int.keys():
            res1 += unicode_in_int[i]
        else:
            res1 += i

    res2 = ''
    for i in second_tuple[0][-1]:
        if i in unicode_in_int.keys():
            res2 += unicode_in_int[i]
        else:
            res2 += i
    res=0
    if int(res1) >= int(res2):
        res = res1    
    else:
        res = res2

    print("Максивальная степень равна:", int(res))
    return int(res)

tuple_of_equation1 = tuple_equation(new_equation_5_1)
tuple_of_equation2 = tuple_equation(new_equation_5_2)
print()

#?  Максимальная степень равна:
find_max_degree = max_degree(tuple_of_equation1, tuple_of_equation2)
# print(type(find_max_degree))

for i in range(len(tuple_of_equation1)):
    for j in range(len(tuple_of_equation2)):
        if tuple_of_equation1[i][-1] == tuple_of_equation2[j][-1]:
            tuple_of_equation2[j] = (str(int(tuple_of_equation1[i][0]) + int(tuple_of_equation2[j][0])), tuple_of_equation1[i][-2], tuple_of_equation1[i][-1])
            break
    else:
        tuple_of_equation2.append(tuple_of_equation1[i])

tuple_of_equation2 = sorted(tuple_of_equation2, key=lambda x: unicode_in_int[x[-1]], reverse=True)    

# print(tuple_of_equation2)

res = ''
for i in range(len(tuple_of_equation2)):
    tuple_of_equation2[i] = list(tuple_of_equation2[i])
    if tuple_of_equation2[i][-1] == '¹':
        tuple_of_equation2[i][-1] = ''
    res += ''.join(tuple_of_equation2[i]) + "+"
    

res = res.replace("+-", "-")[:-1] + " = 0"
print(res)


#?  40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
# Создать новый кортеж
# Дальше сравнивать степени [i][-1]

# Если степени нет, но есть "х", то суммируем, если есть только в одном списке пишем его
# Если степени и "х" нет, то пишем просто число
# перевести кортеж в список

# в конце добавить " = 0"
# print(*новый список)
