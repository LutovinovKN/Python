test = [
    {
    "name": "Константин",
    "surname": "Лутовинов",
    "phones": "89515063050",
    "b-day": "14.07.1991",
    "work": "Рниирс"
    },
    {
    "name": "Елена",
    "surname": "Лутовинова",
    "phones": "89516034582",
    "b-day": "28.11.1991",
    "work": "1forma"
    },
    {
    "name": "Иван",
    "surname": "Иванов",
    "phones": "89516088582",
    "b-day": "28.11.1991",
    "work": "1forma"
    },
    {
    "name": "Иван",
    "surname": "Лутовинов",
    "phones": "89516034582",
    "b-day": "19.03.1989",
    "work": "1forma"
    }
]

find_word = input("введите слово: ")

result = [z for z in test if z["name"] == find_word or z["surname"] == find_word]

if not result:
    print("нет контакта")
else:
    print(result)
