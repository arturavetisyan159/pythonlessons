# задание 3: вывод уникальных букв из двух строк

set1 = set(input('Введите превую строку: '))
set2 = set(input('Введите вторую строку: '))

res = set1.symmetric_difference(set2)
print('Искомыми буквами являются:')
print(*res)
