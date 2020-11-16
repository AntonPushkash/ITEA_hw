"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
a = int(input('Enter number: '))
operator = input('Enter operator: ')

while True:
    b = int(input('Enter number: '))
    if operator == '+':
        answer = a + b
        print(answer)
    elif operator == '-':
        answer = a - b
        print(answer)
    elif operator == '*':
        answer = a * b
        print(answer)
    elif operator == '/':
        answer = a / b
        print(answer)
    else:
        print('wrong operator')

    if input("Continue? (y/n): ") == 'n':
        break
    pass
    a = answer

else:
    print('Bye!')