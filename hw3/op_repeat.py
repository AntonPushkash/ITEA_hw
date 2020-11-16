"""
    Программа принимает на ввод 5-ти значное число.
    Заменяет каждую вторую цифру на 0 и выводит результат.

    [in] 12345
    [out] 10305

    * Если введено не 5-ти значное число
        либо не число обработать и вывести соответствующее сообщение.
"""
try:
    a = int(input('Enter 5 digits number: '))

    first_digit = a // 10000
    second_digit = a % 10000 // 1000
    third_digit = a % 1000 // 100
    forth_digit = a % 100 // 10
    fifth_digit = a % 10

    second_digit = 0
    forth_digit = 0
except ValueError:
    print('You cannot type letters')
else:
    if a < 9999 or a > 99999:
        print("that is not 5 digits number")
    else:
        print(first_digit, second_digit, third_digit, forth_digit, fifth_digit)