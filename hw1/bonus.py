# 1.
# Программа принимает на ввод 4 числа.
# Необходимо сложить первые два и отдельно вторые два.
# Разделить первую сумму на вторую.
# Выведите результат на экран

# number_1 = int(input('Enter number 1: '))
# number_2 = int(input('Enter number 2: '))
# number_3 = int(input('Enter number 3: '))
# number_4 = int(input('Enter number 4: '))

# var_sum_1 = number_1 + number_2
# var_sum_2 = number_3 + number_4

# division = var_sum_1 / var_sum_2
# print(division)

# 2.
# Программа принимает на ввод 3 значения.
# Если все значения – числа, тогда вывести самое большое и самое маленькое из них,
# иначе вывести все значения.

value_1 = input('Enter value 1: ')
value_2 = input('Enter value 2: ')
value_3 = input('Enter value 3: ')

a = int(value_1)
b = int(value_2)
c = int(value_3)

try:
    if a < b < c:
        print(a, c)
    elif b < a < c:
        print(b, c)
    elif c < b < a:
        print(a, c)
    else:
        print(a, b)
except ValueError:
    print(value_1, value_2, value_3)

# number = [a, b, c]

# if type(number) is int:
#     print(max(number), min(number))
# else:
#     print(value_1, value_2, value_3)

# if a < b < c:
#     print(a, c)
# elif b < a < c:
#     print(b, c)
# elif c < b < a:
#     print(a, c)
# else:
#     print(a, b)    