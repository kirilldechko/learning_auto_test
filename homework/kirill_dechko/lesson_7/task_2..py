"""Задание №2
Дан такой словарь:
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
III
lovelovelovelove
итд
Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)
Помните, что копипаст одного и того же кода - плохо"""
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for keys in words:
    value = 0
    my_keys = []  # Создаем пустой список, в который складываем ключи до выполнения условия цикла
    while value < words[keys]:  # создаем цикл с условием: пока правда, что value меньше значения ключа
        value += 1
        my_keys.append(keys)  # В конец списка my_keys добавляем название ключа
    print("".join(my_keys))  # выводим в консоль "списки", каждая строка отдельно
