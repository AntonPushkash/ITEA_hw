"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
s = input('Please type the text: ')
s = s.split()
count = 0
quantity = 0

for i in s:
    if len(i) > count:
        count = len(i)
        longest_word = i
        quantity += 1
print('The longest word is: ',longest_word)
print('The quantity is: ',quantity)