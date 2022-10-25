# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# path = "Test_sem5.md"
# f = open(path, "r")
# data = f.read().split()
# print(*data)
# f.close()

# data = list(map(int, data))
# print(data)
# for i in range(len(data) - 1):
#     if data[i] + 1 == data[i + 1]:
#         continue
#     else:
#         print(data[i] + 1)
        

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
#! Порядок элементов менять нельзя.

# *Пример:* 

#? [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Dict = []
# list_1 = [1, 5, 2, 3, 4, 6, 1, 7]
# list_2 = [list_1[0]]
# num = 1
# for i in list_1:
#     if i == num + 1:
#         list_2.append(i)
#         num += 1
# Dict.append(list_2)        
# print(Dict)
# 




# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв 

# str_abv = "абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв"
# abv = str_abv.split()
# print(abv)

# for i in range(len(abv)):
#     if abv[i].find('абв'):
#         a = abv.pop(i)
# print(abv)
# unicode_in_int = {  "²": 178 - 176,
#                     "³": 3,
#                     "⁴": 4,
#                     "⁵": 5,
#                     "⁶": 6,
#                     "⁷": 7,
#                     "⁸": 8,
#                     "⁹": 9
#                 }
# print(unicode_in_int["²"])
# index_in_int = {"²": '2',
#     "³": '3',
#     "⁴": '4',
#     "⁵": '5',
#     "⁶": '6',
#     "⁷": '7',
#     "⁸": '8',
#     "⁹": '9'
#     }

# line = '²³'
# res = ''

# for i in line:
#     if i in index_in_int.keys():
#         res += index_in_int[i]
#     else:
#         res += i

# print(res)
# B = "²"
# a = ord(B)

# c = chr(a)
# print(unicode_in_int["²"])
t = ('275', '54000', '0.0', '5000.0', '0.0')
lst = list(t)
lst[0] = '300'
t = tuple(lst)