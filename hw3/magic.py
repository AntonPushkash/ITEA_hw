"""
    Магическое число.
    При запуске программы генерируется число, которое нужно угадать.
    Подсказки: больше или меньше.
    Программа в бесконечном цикле.
    После отгадывания появляется результат: само число, количество попыток,
        а так же вопрос: "Continue? (y/n)"

    * Для генерации случайного числа можно воспользоваться
        функцией random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
"""

import random
random_number = random.randint(1, 100)

while True:
    a = int(input('Enter number from 1 to 100: '))

    efforts = 0
    if a == random_number:
        print('You guess!!!')
    else:
        while a != random_number:
            if a > random_number:
                print('It is smaller number!')
            else:
                print('It is bigger number!')

            if a == random_number:
                break
            a = int(input('Enter number from 1 to 100: '))
            efforts += 1
        else:   
            print(a)
            print(efforts)
    if input("Continue? (y/n): ") == 'n':
        break

