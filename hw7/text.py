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
# breakpoint()

with open('text.txt') as f:
    line_list = list(f)
    for line in line_list:
        subline_list = line.split()
        subline_list.reverse()
        subline_list.remove(0)
        subline_list.remove(-1)
        subline_list.insert(0, subline_list[0].capitalize())
        subline_list.insert(-1, subline_list[-1].lower())
        # for i in subline_list:
        #     i.capitalize()
        #     print(i + '\n')
        # if subline_list.index == 0:
        #     subline_list[0].capitalize()
            # subline_list.insert(0, i)
        # elif subline_list.index == -1:
        #     subline_list[-1].lower()
            # subline_list.insert(-1, i)
        # else:
        #     pass
        print(subline_list)

# import pdb; pdb.set_trace()

        # with open('edited_text.txt', 'w') as fe:
        #     fe.writelines(subline_list + '\n')