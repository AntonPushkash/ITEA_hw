"""
    Пользователь вводит количество групп n.
    Далее вводится n строк, каждая строка начинается с названия группы,
    а затем через пробел идут элементы группы.

    1. Обработать строки и вывести на экран словарь, в котором
    ключи - это группы, а значения - списки элементов групп.
    2. Создать и вывести второй словарь, в котором
    ключи - элементы групп, а зачения - группы.

    Используйте функции!

    Например:
    [out] Введите кол-во групп:
    [in]  2

    [out] 1 группа:
    [in]  fruits apple banana mango kiwi lemon

    [out] 2 группа:
    [in]  citrus lime lemon orange

    [out] {
        'fruits': ['apple', 'banana', 'mango', 'kiwi', 'lemon'],
        'citrus': ['lime', 'lemon', 'orange']
    }
    [out] {
        'apple': ['fruits'],
        'lemon': ['citrus', 'fruits'],
        ...
    }
"""
def tmp_dict(n):
    a = {}
    for gr_num in range(n):
        elements_str = input(f'{gr_num + 1} group: ')
        el_list = elements_str.split()
        a.update({el_list[0]: el_list[1:]})
    return a


def main():
    n = int(input('Groups qty: '))
    dict_1 = tmp_dict(n)
    print(dict_1)
    # dict_2 = mod_dict(dict_1)
main()


