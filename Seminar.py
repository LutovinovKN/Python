# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел. 









# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. 
string_list = ['asd', 'okkd', 157, 'jdhy', 1547]
for i in string_list:
    if type(i) == int:
        print(f'{i} - число')







# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# # *Пример:*

# # - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# # - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# # - список: [], ищем: "123", ответ: -1 
# 4. Написать программу проверяющую правильность написания выражения со скобками.

# # {(())}([]{{[]}}) - правильно {[)}(){)) - неправильно *указать где ошибка 
def check_brackets(brc):
    stack = []
    brc_open = {'(': ')', '[': ']', '{': '}'}
    for i in range(len(brc)):
        if brc[i] in brc_open.keys():
            stack.append(brc[i])
        elif brc[i] in brc_open.values():
            if len(stack)>0:
                b = stack.pop()
                if brc_open[b] != brc[i]:
                    return i 
            else: return i 
        if len(stack) == 0:
            return 0
        else:
            return len(brc)
    print(check_brackets('([11]{{[33]}})')) 
    s = '([1+1]{{[3**5]}))-3})' print(s) pos = check_brackets(s) if pos > 0: st = ' '*pos print(f'{st}^') 
# # Write a function unpack() that unpacks a list of elements that can contain objects(int, str, list, tuple, dict, set) 
# # within each other without any predefined depth, meaning that there can be many levels of elements contained in one another.

# # Example:

# # unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]) == [None, 1, 2, 3, 'foo', 'bar']


# # Note: you don't have to bother about the order of the elements, especially when unpacking a dict or a set. 
# # Just unpack all the elements. 
# # For a given list of integers, return the index of the element where the sums of the integers to the left and right of the current element are equal.

# # Example:

# # ints = [4, 1, 7, 9, 3, 9]
# # # Since 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3

# # ints = [1, 0, -1]
# # # Returns None/nil/undefined/etc (depending on the language) as there
# # # are no indices where the left and right sums are equal
# # Here are the 2 important rules:

# # The element at the index to be returned is not included in either of the sum calculations!
# # Both the first and last index cannot be considered as a "midpoint" (So None for [X] and [X, X]) 