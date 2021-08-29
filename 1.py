# Задание 1: удалить символы между первой и последней буквой 'h'

s = 'I am learning Python. hello WORLD!'
str_list = s.split('h')

res = str_list[0] + str_list[len(str_list) - 1]
print(res)

