"""
    Дан файл с текстом (text.txt).
    Создать новый файл (edited_text.txt), каждая строка которого получается из
    соответствующей строки исходного файла с обратным порядком слов, причем
    первое слово с заглавной буквы, а все остальные со строчной.

    Например 1 файл содержит:
    Hello world
    How are you

    Тогда второй файл будет содержать:
    World hello
    You are how
"""

with open('text.txt') as f:
    with open('edited_text.txt', 'w') as fe:
        for line in f.readlines():
            line_list = line.split()
            line_list.reverse()
            s = ' '.join(line_list).capitalize()
            fe.write(s + '\n')