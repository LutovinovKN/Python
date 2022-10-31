#    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('/home/sideshow/GeekBrains/Семинар/Python/Lesson_5/Task_4/Task_4_input.txt', 'r') as data:
    input_text = data.read()
print(input_text)
def encode_rle(num):
    str_code = ''
    prev_char = ''
    count = 1
    for char in num:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    if prev_char == 1:
        str_code += prev_char
    else:
        str_code += str(count) + prev_char
    return str_code

            
str_code = encode_rle(input_text)
print(str_code)
with open("/home/sideshow/GeekBrains/Семинар/Python/Lesson_5/Task_4/Task_4_output.txt", "w") as file:
    file.write(str_code)
# print(str_decode)

with open('/home/sideshow/GeekBrains/Семинар/Python/Lesson_5/Task_4/Task_4_output.txt', 'r') as data:
    output_text = data.read()
# path = "/home/sideshow/GeekBrains/Семинар/Python/Lesson_5/Task_4/Task_4_output.txt"
# f = open(path, 'r')
# output_text = f.read()
# f.close

def decoding_rle(num:str):
    count = ''
    str_decode = ''
    for char in num:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(output_text)
with open("/home/sideshow/GeekBrains/Семинар/Python/Lesson_5/Task_4/Task_4_decoding.txt", "w") as file:
    file.write(str_decode)
if input_text == str_decode:
    print("Восстановленный код соответствует первоначальному")
else:
    print("где-то произошла ошибка")