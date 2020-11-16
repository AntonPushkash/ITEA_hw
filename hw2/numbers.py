"""
    Дано число от 1 до 999.
    1. Найти сумму цифр числа. (для 2-знач числа - lesson1/3_practice_operators.py)
    2. Вывести, в каком порядке расположены цифры (возрастания/убывания/в разброс)
"""

try:
    number = int(input())
    d1 = number // 10
    d2 = number % 10
    d3 = number // 100
    d4 = number % 100 // 10
    d5 = number % 100 % 10
except ValueError:
    print('Enter the number from 1 to 999')
else:
    if 1 <= number <= 99:
        print(d1 + d2)
    elif 999 >= number >= 99 :
        print(d3 + d4 + d5)
    else:
        print('Enter the number from 1 to 999')

if 1 <= number <= 99 and d1 < d2:
    print('accending')
elif 1 <= number <= 99 and d1 > d2:
    print('deccending')
elif 999 >= number >= 99:
    if d3 <= d4 <= d5:
        print('accending')
    elif d3 >= d4 >= d5:
        print('deccending')
    else:
        print('disorder')
else:
    pass


