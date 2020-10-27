"""
    Необходимо написать простой калькулятор, который принимает на ввод:
    первое число, второе число и оператор
    В зависимости от введенного оператора, между числами проводится определенная операция.
    Результат операции выводится на экран.
"""
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
operator = input('Enter operator: ')

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
else:
    print(a / b)