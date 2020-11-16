"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""
import re

number = input('Enter your phone: ')
count = 0

for i in number:
    if i.isdigit():
        count += 1

new_number = re.sub(r'\D', '', number)

if count <= 12:
    print('The phone is ', '+380' + new_number[-9:])
else:
    print('Longer number than requested')