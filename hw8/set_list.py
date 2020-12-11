"""
    Реализовать функции, которые принимают 2 списка чисел и:

    1 функция
    Возвращает список чисел (в порядке возрастания),
    которые содержатся в первом и втором списке одновременно.

    2 функция
    Возвращает список чисел (в порядке убывания),
    которые не содержатся в первом и втором списке одновременно.

    3 функция
    Возвращает количество уникальных чисел,
    которые содержатся во втором списке, но не содержатся в первом.
"""
def assend_list(a, b):
    c = sorted(a.intersection(b))
    return c

def dessend_list(a, b):
    d = sorted(a.symmetric_difference(b), reverse=True)
    return d

def uniq_list(a, b):
    e = len(a.difference(b))
    return e

def main():
    a = set(input('List 1: ').split())
    b = set(input('List 2: ').split())
    assend_set = assend_list(a, b)
    print(assend_set)
    dessend_set = dessend_list(a, b)
    print(dessend_set)
    uniq_set = uniq_list(a, b)
    print(uniq_set)

main()