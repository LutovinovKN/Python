# + 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#  *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
# f = x*-3

# a = int(input('Введите число a: '))

# def is_int(a):
#     try:
#         int(a)
#         return True
#     except ValueError:
#         return False

# list = []

# # for i in range(1, a+1):
# #     print(i*-3)

# for i in range(1, a+1): # а теперь списком
#     list.append(i*-3)

# print(list)

# ----------------------------------------------------

# + 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число n: '))

# dictionary = {}
# for i in range(1, n+1):
#     dictionary[i] = 3*i + 1
# print(dictionary)

# ----------------------------------------------------

# + 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.

# num1 = input('Введите строку: ')
# print(num1)
# num2 = input('Введите строку: ')
# print(num2)

# print(num1.count(num2))

# ---------------------------------
# + Write a function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. You can guarantee that input is no
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

# number = int(input('Введите число: '))

# binar_number = bin(number)
# print(binar_number)

# print(binar_number.count('1'))

# ----------------------------------

# + Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
# with the same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# line = input('Введите строку: ')
# # line = 'AAAABBBCCDAABBB'
# # line = 'ABBCcAD'
# # line = [1,2,2,3,3]

# list_line = []
# list_line.append(line[0])

# for i in range(len(line)-1):
    
#     if line[i] != line[i+1]:
#         list_line.append(line[i+1])
#     else: continue

# print(list_line)

# ----------------------------------
# Create a function taking a positive integer as its parameter and returning a string 
# containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the 
# left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 
# 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:
# solution(1000) # should return 'M'
# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.

# num = int(input('Введите число: '))
# result = ''

# while num >= 1:
#     if num >= 1000:
#         count_m = num // 1000
#         for i in range(count_m):
#             rom = 'M'
#             result = result + rom
#         num %= 1000
#     if num >= 500:
#         count_d = num // 500
#         if count_d <= 3:
#             for i in range(count_d):
#                 rom = 'D'
#                 result = result + rom
#             num %= 500
#         else:
#             rom = 'DM'
#             result = result + rom
#             num %= 500
#     if num >= 100:
#         count_c = num // 100
#         if count_c <= 3:
#             for i in range(count_c):
#                 rom = 'C'
#                 result = result + rom
#             num %= 100
#         else:
#             rom = 'CD'
#             result = result + rom
#             num %= 100        
#     if num >= 50:
#         count_l = num // 50
#         for i in range(count_l):
#             rom = 'L'
#             result = result + rom
#         num %= 50        
#     if num >= 10:
#         count_x = num // 10
#         for i in range(count_x):
#             rom = 'X'
#             result = result + rom
#         num %= 10    
#     if num >= 5:
#         count_v = num // 5
#         for i in range(count_v):
#             rom = 'V'
#             result = result + rom
#         num %= 5
#     if num >= 1:
#         count_i = num // 1
#         for i in range(count_i):
#             rom = 'I'
#             result = result + rom
#         num %= 1

# print(result)
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

