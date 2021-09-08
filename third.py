# Задача 3: валидация номера телефона.

import re

s = input('Введите номер телефона => ')
reg = r'\d'

numbers = re.findall(reg, s)

res_number = ''
for num in numbers:
    res_number += num
if res_number[0] != 7:
    res_number = '7' + res_number[1:len(res_number)]

res = '+' + res_number[0] + ' ' + '(' + res_number[1:4] + ')' + ' ' + res_number[4:7] + '-' + res_number[7:9] + '-' + res_number[9:11]

print(res)