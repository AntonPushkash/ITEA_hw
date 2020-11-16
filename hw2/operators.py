"""
    Даны 3 челых числа.
    1. Найти сумму тех чисел, которые делятся на 5, иначе вывести сообщение.
    2. Найти количество положительных чисел.
    3. Найти количество отрицательных чисел.
    4. Найти сумму 2х найбольших чисел.

    Вывести сообщение типа:

    Числа: -10, 4, 21
    1. -10
    2. 2
    3. 1
    4. 25
"""

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
sum = a + b + c

if sum % 5 == 0:
    print(sum)
else:
    print('You cannot divide by 5')

if a > 0 or b > 0 or c > 0:
    print(bool(a > 0) + bool(b > 0) + bool(c > 0))
elif a < 0 and b < 0 and c < 0:
    print('0')
else:
    pass

if a < 0 or b < 0 or c < 0:
    print(bool(a < 0) + bool(b < 0) + bool(c < 0))
elif a > 0 and b > 0 and c > 0:
    print('0')
else:
    pass

if a < b < c:
    print(b + c)
elif b < a < c:
    print(a + c)
elif c < b < a:
    print(b + a)
elif b < c < a:
    print(c + a)
else:
    print('all numbers are equal')