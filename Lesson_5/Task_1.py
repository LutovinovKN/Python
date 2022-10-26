#   Напишите программу, удаляющую из текста все слова, содержащие "абв".
def out_yellow(text):
    print("\033[33m {}" .format(text))

def del_some_words(text, find_word):
    text = list(filter(lambda x: find_word not in x, text.split()))
    return " ".join(text)

proposal_str = input('Введите текст, который хотите проверить: \n').lower()
find_str = input("Введите набор символов, которые нарушают правильное написание слова и мы удалим эти слова: \n").lower()

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

my_text = del_some_words(proposal_str, find_str)
out_yellow(my_text)