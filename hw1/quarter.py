"""
    Программа принимает на ввод координату x и y точки.
    Выводит, в какой четверти системы координат лежит точка.

                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""
x = int(input('Enter coordinate x: '))
y = int(input('Enter coordinate y: '))

if x < 0 and y < 0:
    print('III')
elif x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
else:
    print('IV')