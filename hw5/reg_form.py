"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

        Программа выводит сообщение:

        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********

"""
import re

def main():
    phone = input_phone()
    email = input_email()
    password = input_password()
    print('Поздравляем с успешной регистрацией!')
    print(f'Ваш номер телефона: {phone}')
    print(f'Ваш email: {email}')
    print(f'Ваш пароль: {password}')

def input_phone():
    number = input('Enter your phone: ')
    new_number = re.sub(r'\D', '', number)

    if len(new_number) > 12:
        print('Longer number! Try again!')
        return input_phone()
    elif len(new_number) < 12:
        print('Short number! Try again!')
        return input_phone()
    return '+380' + new_number[-9:]

def input_email():
    email = input('Enter your email: ')

    if len(email) < 6 and email.count('@') != 1:
        print('Wrong email! Try again!')
        return input_email()
    return email

def input_password():
    password = input('Enter the password: ')

    upper = lower = digit = space = 0
    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1

    if len(password) < 8 or space != 0 or upper < 1 or lower < 1 or digit < 1:
        print('Wrong password! Try again!')
        return input_password()
    
    password_confirm = input('Confirm the password: ')

    if password != password_confirm:
        print('Missmached password! Try again!')
        return input_password()
    return password

main()
