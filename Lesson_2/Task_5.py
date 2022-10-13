# Реализуйте алгоритм перемешивания списка.

from random import randint

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9]
res = [x for y in zip(numbers2, numbers1) for x in y]
print(res)