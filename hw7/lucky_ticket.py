"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""
ticket_num = 479974


def is_lucky(ticket_num):
    list_num = [int(i) for i in str(ticket_num)]
    list_len = len(list_num)
    qty_idx = list_len / 2
    list_1 = []
    list_2 = []
    index = 0
    for num in list_num:
        if num[index] <= qty_idx:
            list_1.append(num)
            index += 1
        else:
            list_2.append(num)
            index += 1
    if sum(list_1) == sum(list_2):
        return bool
    else:
        bool


result = is_lucky(ticket_num)
print(result)

# assert is_lucky(1230) is True
# assert is_lucky(239017) is False
# assert is_lucky(134008) is True
# assert is_lucky(15) is False
# assert is_lucky(2020) is True
# assert is_lucky(199999) is False
# assert is_lucky(77) is True
# assert is_lucky(479974) is True
