"""
    Выполните все пункты.

    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое


# 2.
with open('file_practice.txt') as f:
    f.seek(0)
    print(f.read(5))

# 3.
i_counter = e_counter = 0
with open('files/text.txt') as f:
    data = f.read()
    for l in data:
        if l == 'i':
            i_counter += 1
        elif l == 'e':
            e_counter += 1
    
if i_counter > e_counter:
    edited = open('files/text.txt', 'r').read().replace('i', 'e')
else:
    edited = open('files/text.txt', 'r').read().replace('e', 'i')

with open('files/text.txt', 'a+') as f:
    f.write(edited)

# 4.
with open('files/text.txt', 'a+') as f:
    f.write('*some pasted text*')
    pos = (f.tell())
    if pos % 2 == 0:
        f.write('\nthe end')
    else:
        f.write('\nbye')

with open('files/text.txt') as f:
    print(f.read())