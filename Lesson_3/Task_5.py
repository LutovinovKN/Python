#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#*     Пример:
#*      для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

while True:
    try:
        n = int(input('with what number do you want to view the Fibonacci Sequence? Enter a number: '))       
    except ValueError:
        print("Not an integer number!")
        continue
    else:
        print("Yes an integer number!")
        break 

fibonacci = [0, 1]
anti_fibonacci = [1, 0]

for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    anti_fibonacci.insert(0, anti_fibonacci[1] - anti_fibonacci[0])

# print(fibonacci)
# print(anti_fibonacci)
if n == 0:
    print([0])
else:
    anti_fibonacci.extend(fibonacci[1:])
    print(anti_fibonacci)
