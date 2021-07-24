# Задание 3 - статистика частотности символов в кортеже

tpl1 = tuple(input('Введите по порядку без пробелов элементы кортежа: '))
print(tpl1)
lst = []
for element in tpl1:
    if element in lst:
        continue
    else:
        lst.append(element)

for el in lst:
    print('Количество', el, '=', tpl1.count(el))