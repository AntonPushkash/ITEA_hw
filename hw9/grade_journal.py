"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""
def swap_items(a):
    return {v: k for k, v in a.items()}


def main():
    n = int(input('Enter the quantity: '))
    d = {}
    for key, value in a.items():
        print(key, value)
    key_list = list((input('Enter the keys: ')).split())
    values_list = list((input('Enter the values: ')).split())
    a = dict(zip(key_list, values_list))
    print(a)
    print(swap_items(a))

main()