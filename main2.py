

########################################################################################################################
                                # Словари (dictionary)
########################################################################################################################

# d = {'one': 1, 'two': 2}
# print(d)
#
# a = {}
# # print(type(a)) # <class 'dict'>
#
# d1 = dict(one='one1', two=2)
# # print(type(a1)) # <class 'dict'>
# print(d1)
#
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3) # {'a': 100, 'b': 100}

##############################

# users = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna']
# ]
#
# d_users = dict(users) # Если в списке правильно расположены элементы, то все сгенерируется нормально
# print(d_users) # {'igor@gmail.com': 'Igor', 'irina@gmail.com': 'Irina', 'anna@gmail.com': 'Anna'}

##############################

# d4 = {a+5: a ** 2 for a in range(7)}
# print(d4)
#
# print(d4[7]) # 4 - обращение к элементу по ключу
# d4[7] = 14
# print(d4[7]) # 14

##############################
# d5 = {0: 'text1', 'one': 45, (1, 2.3): 'кортеж', 42: [1, 2, 3, 6], True: 1}
# print(d5[42][1]) # 2
# print(d5['one'])
# del d5[(1, 2.3)] # удаляет ключ и значение в словаре
# print(d5)
#
# print('one' in d5) #  True
# print('two' in d5) # False
# print(d5.keys())
#
# if 'one' in d5: # проходит по всем элементам
#     print('TRUE')
# if "one" in d5.keys(): # проходит только по ключам
#     print("TRUE")

##############################
# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6['four'])
# key = "four"
# # if key in d6:
# #     del d6[key]
# try:
#     del d6[key]
# except KeyError:
#     print("Такого ключа нет в словаре!")
# print(d6)

##############################
# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, d6[key])

##############################
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res = res * d[key]
# print(res) # -105

##############################
# Задача: наполнить словарь, потом удалить элемент по ключу

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# key = int(input('Какой элемент исключить: '))
# del d[key]
# print(d)

##############################
# capitals = dict()
#
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ': ' + capitals[country])
#     else:
#         print('В базе нет страны с названием ' + country)

##############################
# Задание: данные о товарах, их количестве и цене. Реализовать изменение количества товара по ключу

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670k', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for key in goods:
#     print(key + ') ' + goods[key][0] + ' - ' + str(goods[key][1]) + ' шт. По ' + str(goods[key][2]) + ' руб.')
# print()
# change_key = 1
# while change_key != 0:
#     change_key = int(input('№: '))
#     if change_key != 0:
#         amount = int(input('Количество: '))
#         goods[str(change_key)][1] = amount
#     else:
#         break
#
# for key in goods:
#     print(key + ') ' + goods[key][0] + ' - ' + str(goods[key][1]) + ' шт. По ' + str(goods[key][2]) + ' руб.')

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# value = d.get('B')
# print(value) # 2

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# value = d.get('E', 'FF')
# print(value) # FF
# print(d) # {'A': 1, 'B': 2, 'C': 3} (Словарь не изменился!)

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# new = d.items() #  возвращает список с кортеами (ключ, значение)
# print(new)
# a = d.keys()
# print(a)

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# item = d.popitem()
# print(item) # ('C', 3)
# print(d) # {'A': 1, 'B': 2}

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# item = d.setdefault("B")
# print(item) # 2

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# d.update([("R", 1), ("Q", 9)]) # обновляет словарь. Если ключа нет, то он появляется с зад значением, если есть - перезапись
# print(d)

##############################
# Задача: объеденить два словаря

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# x.update(list(y.items()))
# print(x)

##############################
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y # объединение.
# print(z)

##############################
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {i: d[i] for d in [x, y] for i in d}
# print(z) # {'a': 1, 'b': 3, 'c': 4}

##############################
# d = {'A': 1, 'B': 2, 'C': 3}
# v = d.values() # возвращет список значений
# print(v)

##############################
# Задание
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d_new = {}
# d_new['name'] = d.pop('name')
# d_new['salary'] = d.pop('salary')
# print('новый словарь:', d_new)
# print('исходный словарь:', d)

##############################
# Задание: заменить 'city' на 'location'
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# city = d.pop('city')
# d.update([('location', city)])
# print(d)

##############################
# a = {
#     "first": {
#         1: 'one',
#         2:'two',
#         3:'three'
#     },
#     "second": {
#         4: 'four',
#         5: 'five'
#     }
# }
# # print(a["first"][2]) # two
#
# for x in a:
#     print()
#     print(x, ':', sep='')
#     for y in a[x]:
#         print(y, ':', ' ', a[x][y], sep='')

##############################
# Задание:

# sellings = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4835,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451
#     }
# }
# for x in sellings:
#     print()
#     print(x, ':', sep='')
#     for y in sellings[x]:
#         print(y, ':', ' ', sellings[x][y], sep='')
#
# print()
# print()
# name = input('Имя: ')
# region = input('Регион: ')
# print(sellings[name][region])
# new_value = int(input('Новое значение: '))
# sellings[name][region] = new_value
#
# print(sellings[name])

##############################
# a_dict = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_dict = {value: key for key, value in a_dict.items()}
# print(new_dict)

##############################
# Вывести первые два элемента

# a_dict = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# m = list(a_dict.items())
# new_dict = {m[x][0]: m[x][1] for x in range(0, 2)}
# print(new_dict)

##############################
# a = {i: i * 5 for i in[10, 20, 30, 40]}
# # print(a)

##############################
# s = 'Hello'
# b = {i: i * 3 for i in s}
# print(b)

##############################
# value = int(input('-> '))
# lt = [1, 2, 3, 4]
# d = {k: value for k in lt}
# print(d)

##############################
# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[2, 0] = 2

# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))

# try:
#     print(m[(2, 1)])
# except:
#     print(0)

# if (2, 1) in m:
#     print(m[(2, 1)])
# else:
#     print(0)

##############################
# ЗАДАЧА преобразовать в словарь

lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
d = {}

for i in range(0, len(lst)):
    values = []
    j = 0
    if type(lst[i]) == str:
        k = i
        while type(j) != str:
            if type(j) == str:
                break
            if k == len(lst) - 1:
                break
            j = lst[k + 1]
            k = k + 1
            values.append(j)
        d.update([(lst[i], values)])

