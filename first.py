# Задание 1: проверка пароля
import re

def password_check():
    password = input('Введите пароль: ')
    reg= '[^0-9a-zA-z@_-]'
    if len(password) >= 6 and len(password) <= 16 and len(re.findall(reg, password)) == 0:
        print('Все сработало, ваш пароль: ' + password)
    else:
        print('Введите праоль еще раз, так как он не соответствует требованиям.')
        return password_check()

password_check()