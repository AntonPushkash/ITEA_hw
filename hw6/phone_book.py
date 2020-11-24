"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).

    Перед записью в файл привести номер к формату +380501234567.
"""
import re

with open('files/phone_book.txt') as f:
    for i in f:
        s = re.sub(r'\W', '', i)
        letters = re.sub(r'\d', '', s)

        digits = (re.sub(r'\D', '', s)[-9:])
        ed_user = f'{letters} +380{digits}'
        if ed_user.startswith('М') is True or ed_user[-15] == 'а':
            print(ed_user)

            with open('files/edited_phone_book.txt', 'a+') as fe:
                fe.writelines(ed_user + '\n')
