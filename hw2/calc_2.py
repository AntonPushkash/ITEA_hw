"""
    Обновить калькулятор из 1 дз.
    1. Если введены не числа, выводить соответствующее сообщение.
    2. Обрабатывать деление на 0.
"""
# a = int(input('Enter number 1: '))
# b = int(input('Enter number 2: '))
# operator = input('Enter operator: ')

try:
    a = int(input('Enter number 1: '))
    b = int(input('Enter number 2: '))
    operator = input('Enter operator: ')
except ValueError:
    print('You cannot type letters')
else:
    if operator == '+':
        print(a + b)
    elif operator == '/':
        if b == 0:
            print('You cannot divide by 0')
        else:
            print(a / b)
    elif operator == '*':
        print(a * b)
    else:
        print(a - b)