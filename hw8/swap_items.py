"""
    Напишите функцию, которая принимает словарь,
    меняет местами ключи и значения и возвращает его.

    Покройте функцию несколькими тестами.

    Пример:
    a = {'key': 'value', 'd': 1234}
    b = swap_items(a)
    print(b)
    {'value': 'key', 1234: 'd'}

    * пропускайте пары, в которых значение не может быть ключем

    ** ключем словаря может быть только не изменяемый объект,
        а точнее тот, который можно захешировать функцией hash()

"""

def swap_items(a):
    return {v: k for k, v in a.items()}


def main():
    key_list = list((input('Enter the keys: ')).split())
    values_list = list((input('Enter the values: ')).split())
    a = dict(zip(key_list, values_list))
    print(a)
    print(swap_items(a))

main()

assert swap_items({'user1': 'value1', 'user2': 'value2'}) == {'value1': 'user1', 'value2': 'user2'}
