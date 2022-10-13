# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
#*  6782 -> 23
#*  0,56 -> 11

number= float(input("Enter a number: "))*100
sum_number = 0
last_digit = 0

for i in range(len(str(number))):
    last_digit = number % 10
    sum_number += last_digit
    number //= 10
    

print(int(sum_number))
