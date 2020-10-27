# 1.
# Программа принимает на ввод 4 числа.
# Необходимо сложить первые два и отдельно вторые два.
# Разделить первую сумму на вторую.
# Выведите результат на экран

number_1 = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))
number_3 = int(input('Enter number 3: '))
number_4 = int(input('Enter number 4: '))

var_sum_1 = number_1 + number_2
var_sum_2 = number_3 + number_4

division = var_sum_1 / var_sum_2
print(division)