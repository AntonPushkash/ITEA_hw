"""
    Вводится строка.

    (!!! 1 пункт не изменяет строку, а 2 и 3 - изменяют !!!)

    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f, format либо %)
"""
s = input('Initial text: ')

# 1 solution
count_upper = count_lower = count_words = 0
for i in s:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1

if count_upper > count_lower:
    print('Result_1: ', s.upper())
elif count_upper < count_lower:
    print('Result_1: ', s.lower())
else:
    print('Result_1: ', s.swapcase())

# 2 solution
if s.istitle():
    print('Result_2: ','done', s)
else:
    print('Result_2: ', s[:5])


# 3 solution
if len(s) < 20:
    print('Result_3: ', s.ljust(20, '@'))
else:
    print('Result_3: ', s[:20])