"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно (не влияет на оценку):
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""

import random
import string
from random import randint, sample
from string import ascii_letters as let, ascii_lowercase as low
from string import punctuation as pun, digits, ascii_uppercase as upp

print('Choose the password')
password = int(input("if simple enter '1', if middle enter '2', if difficult enter '3'"))

if password == 1:
    simple_pass = sample(low, 8)
    print(''.join(simple_pass))
elif password == 2:
    any_pass = sample(let + digits, 8)
    print(''.join(any_pass))
else:
    pass_len = randint(8, 16)
    var_pass = sample(low + let + digits + pun, pass_len)
    print(''.join(var_pass))

# Дополнительно 1:
    # while True:
    #     pass_len = int(input('Please enter the password length: '))
    #     if pass_len < 8:
    #         print('Unsafe password!!!')
    #         continue
    #     else:
    #         var_pass = sample(low + let + digits + pun, pass_len)
    #         print(''.join(var_pass))

# Дополнительно 2: