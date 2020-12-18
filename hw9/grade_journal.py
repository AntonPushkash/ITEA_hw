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
def sort_keys(d):
    for i in [i[0] for i in (sorted(d.items(), key=lambda x: x[1]))]:
    print(i)


def main():
    n = int(input('Enter the quantity: '))
    d = {}
    for i in range(n):
        affort = list((input('Enter the surname and score: ')).split())
        d.update({affort[0]: affort[1:]})
    print(d)

main()