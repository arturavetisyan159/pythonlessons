# Задача 3: удаление всех вхождений заданного символа из строки.
str1 = '012345363738494'
print(f'str1: {str1}')
symbol = input('Какой символ следует удалить? -> ')
if symbol in str1:
    str2 = ''
    for el in str1:
        if el == symbol:
            continue
        else:
            str2 = str2 + el
    print(f'str2: {str2}')
else:
    print('Такого символа нет в строке!')
