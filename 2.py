# Задача 2: удаление буквы из слова, заданной номером позиции.

str1 = '0123456789'
print(f'str1: {str1}')
index = int(input('С какой позиции удалить символ? -> '))
str2 = str1[:index] + str1[index + 1:]
print(f'str2: {str2}')
