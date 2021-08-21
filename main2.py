

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

# lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
#
# for i in lst:
#     if type(i) == str:
#         key = i
#         d[key] = []
#     if type(i) == int:
#         d[key].append(i)
# print(d)

##############################
#                                   ZIP

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d) # {1: 'one', 2: 'two', 3: 'three'}

##############################
# d = {}
# lst = list(zip([1, 2], [3, 4]))
# print(lst)
# d.update(lst)
# print(d)

##############################
# one = {'name': 'Igor', 'surname': 'Dou', 'job': 'consultant'}
# two = {'name': 'Irina', 'surname': 'Smith', 'job': 'manager'}
#
# for (k1, v1), (k2, v2) in list(zip(one.items(), two.items())):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

##############################
# pairs = [(1, 'a'), (2,'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs) # обратная операция
#
# print(a) # (1, 2, 3, 4)
# print(b) # ('a', 'b', 'c', 'd')

##############################
# l = ['b', 'a', 'd', 'c']
# n = [2, 4, 1, 3]
# s1 = list(zip(l, n))
# print(s1)
# s1.sort() # происходит сортировка по первому элементу кортежа
# print(s1)
#
# print()
#
# s2 = list(zip(n, l))
# print(s2)
# s2.sort()
# print(s2)
#
# print()
#
# d3 = sorted(zip(l, n))
# print(d3)

##############################
# Задание: через zip вывести прибыль.

# months = ['january', 'february', 'march']
# totalSales = [52000, 51000, 48000]
# productionCost = [46800, 45900, 43200]
#
# table = list(zip(months, totalSales, productionCost))
# print(table)
#
# for element in table:
#     print('Прибыль в', element[0], 'составила:', element[1] - element[2])

##############################
# one = {'apple': 0.40, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**two, **one}) # ** - это оператор распаковки словаря.
#
# for k, v in {**two, **one}.items():
#     print(k, '->', v)

##############################
#                            ENUMERATE()
# data = [2, 5, 3, 4, 1, 5]
# for i, val in enumerate(data, 1): # делает список кортежей
#     print(i, val)

##############################
# data = [2, 5, 3, 4, 1, 5]
# itr = iter(data)
# print()
# print(next(itr)) # 2
# print(next(itr)) # 5
# print(next(itr)) # 3
# print(next(itr)) # 4
# print(next(itr)) # 1
# print(next(itr)) # 5
# print(next(itr, 'stop'))

##############################
# data = [2, 5, 3, 4, 1, 5]
# b = enumerate(data)
# c = next(b)
# print(c)
# print(next(b))

##############################
# a = [1, 2, 3]
# b = [*a, 4, 6, 8] # [1, 2, 3, 4, 6, 8]

##############################
# def func(*args): # *a возвращает кортежик
#     if args == tuple():
#         return 0
#     else:
#         mult = 1
#         for el in args:
#             mult = mult * el
#         return mult
# print(func(5))
# print(func(5, 6, 4, 3))
# print(func())

##############################
# def func(*args):
#     return {i: i for i in args}
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8))

##############################
# def func(*args):
# #     sum = 0
# #     for el in args:
# #         sum = sum + el
# #     print('Среднее арифметическое:', sum/len(args))
# #     res_list = []
# #     for elem in args:
# #         if elem < sum/len(args):
# #             res_list.append(elem)
# #     print(res_list)
# #
# # func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# # func(3, 6, 1, 9, 5)

##############################

# def func(student, *args):
#     print(f'Student name: {student}')
#     for i in args:
#         print(i)
#
#
# func('Igor', 100, 96, 88, 92, 99)
# print()
# func('Irina', 96, 20, 33, 36)

##############################
# Задание: поменять порядок цифр в числе

# def func(*args, only_odd=False):
#     res_list = []
#     if only_odd == False:
#         for el in args:
#             el = str(el)
#             new_el = ''
#             for i in range(len(el) - 1, -1, -1):
#                 new_el = new_el + el[i]
#             res_list.append(int(new_el))
#     if only_odd == True:
#         for el in args:
#             if el % 2 != 0:
#                 el = str(el)
#                 new_el = ''
#                 for i in range(len(el) - 1, -1, -1):
#                     new_el = new_el + el[i]
#                 res_list.append(int(new_el))
#             else:
#                 continue
#     return res_list
#
# print(func(12, 23, 41, 5643, only_odd=True)) # [32, 14, 3465]
# print(func(12, 23, 41, 5643)) # [21, 32, 14, 3465]

##############################

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}
# print(func()) # {}
# print(func(a='python')) # {'a': 'python'}

##############################

# def info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, 'is', v)
#     print()
#
# info(firstname='Irina', lastname='Sharm', age=22, phone=1212482)
# info(firstname='Irina', lastname='Wood', email='igor@gmail.com', age=25)

##############################
# Задание: написать функцию, чтоб при каждом ее вызове, обновлялся словарь

# my_dict = {'one': 'first'}
# def db(**kwargs):
#     my_dict.update(kwargs.items())
#
# db(k1=22, kr=11)
# db(m=1)
# print(my_dict)

##############################
# SCOPE - область видимости переменных и др.

# name = "Tom" # глобальная переменная
#
#
# def hi():
#     print('Hello', name)
#
# def bye():
#     print("Good bye", name)
#
# hi()
# bye()
##############################
# name = 'Bob' # глобальная
#
# def hi():
#     print('Hello', name)
#
# def bye():
#     global name # перезаписываем глобальную переменную
#     name = 'b' # локальная
#     print("Good bye", name)
#
# bye()  # b
# hi() # b
# print(name) # b

##############################

# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func() # 5

##############################
# def add_two(a):
#     x = 2
#     def add_some():
#         print('x =', x)
#         return a + x
#     return add_some()
#
# print(add_two(3))

##############################
# x = 25
#
# def outer_func():
#     global t
#     a = 30
#     t = a
#     print(x)
#
#     def inner_func():
#         nonlocal a
#         a = 35
#         print('nonlocal \'a\':', a)
#     inner_func()
#
# outer_func()
# z = x + t
# print(z)


##############################
# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 35
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#         fn3()
#         print('fn2.x1 =', x1) # 55
#
#     fn2()
#     print('fn1.x1 =', x1) # 25
#
# fn1()


##############################

# def increment(number):
#
#     def inner_increment(x):
#         return number + x
#     return inner_increment
#
#
# test1 = increment(10)
# print(test1(5)) # 15
#
# test2 = increment(10)
# print(test2(6)) # 16
#
# print(increment(10)(7)) # 17

##############################

# def increment():
#     # a, b, c - свободные пременные
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def inner_increment():
#         c.append(4)
#         nonlocal a
#         a = a + 1
#         return a, b, c
#
#     return inner_increment
#
#
# test1 = increment()
# print(test1())


##############################
# Задача:

# def visits(city):
#     counter = 0
#     def visits_counter():
#         nonlocal counter
#         counter = counter + 1
#         print(city + ' ' + str(counter))
#     return visits_counter
#
# test1 = visits('Moscow')
# test2 = visits('Sochi')
# test1() # Moscow 1
# test1() # Moscow 2
# test1() # Moscow 3
# test2() # Sochi 1
# test2() # Sochi 2


##############################

# students = {
#     'art': 100,
#     'Anna': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'Alice': 75,
#     'Fiona': 35,
#     'Ella': 54,
#     'David': 69
# }
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#
#     return inner
#
# a = outer(80, 101)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
#
# print(a(students)) # {'art': 100, 'Anna': 98, 'Chris': 85}
# print(b(students)) # {'Alice': 75}
# print(c(students)) # {'Bob': 67, 'Ella': 54, 'David': 69}
# print(d(students)) # {'Fiona': 35}

##############################

# def outer(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mult():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mult = mult
#
#     return replace
#
# obj1 = outer(5, 2)
# print(obj1.add()) # 7
#
# obj2 = outer(5, 2)
# print(obj2.sub()) # 3
#
# obj3 = outer(5, 2)
# print(obj3.mult()) # 10

##############################
#                                        LAMBDA - ФУНКЦИЯ
# func = lambda x, y: x + y
# print(func(10, 5)) # 15
# print(func('a', 'b')) # ab

# print((lambda x, y: x + y)(1, 2)) # 3

# a = (lambda x, y: x + y)(1, 4)
# print(a) # 5

##############################

# print((lambda x, y: x**2 + y**2)(1, 2))

##############################

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10)) # 15

##############################

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4)) # (1, 2, 3, 4)

##############################

# c = (lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
# for t in c:
#     print(t('abc'))

##############################

# def inc(n):
#     return lambda x: x + n

# test1 = inc(5)
# print(test1(2))
# print(test1(2))

##############################

# inc = (lambda n: (lambda x: n + x))
# test1 = inc(5)
# print(test1(2))

# print((lambda n: (lambda x: n + x))(5)(7))

##############################
# circle = lambda r: 3.14 * r ** 2
# sq = lambda w, l: w * l
# trap = lambda a=7, b=5, h=3: (a + b)/2 * h

# print(circle(2))
# print(sq(10, 13))
# print(trap())

##############################

# d = {'a': 10, 'b': 15, 'c': 4}

# list_d = list(d.items())
# print(list_d)

# list_d.sort(key=lambda i: i[1])
# print(list_d)

##############################

# Задача (отсортировать по фамилии, а потом по баллу и по баллу наоборот)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
# print('Сортировка по фамилии', end='\n')
# players.sort(key=lambda i: i['last name'])
# print(players)

# print()

# print('Сортировка по рейтингу', end='\n')
# players.sort(key=lambda i: i['raiting'])
# print(players)

# print()

# print('Наоборот', end='\n')
# players.sort(key=lambda i: i['raiting'], reverse=True)
# print(players)

##############################
# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y)
# ]
# b = a[0](5, 12)
# print(b) # 17

# b = a[1](5, 12)
# print(b) # -7

##############################
# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]

# for i in b: 
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

##############################

# d = {
#     1: (lambda: print('Monday')),
#     2: (lambda: print('Tuesday')),
#     3: (lambda: print('Wednesday')),
# }
# d[1]()

##############################
# maximum = (lambda a, b: a if a>b else b)
# print(maximum(10, 11)) # 11

##############################
# Задача найти минимальное из трех значений:

# minimum = (lambda a, b, c: a if a <= b and a <= c else b if b <= c and b <= a else c)
# print(minimum(9, 8, 5))

##############################
#                                   MAP(funct, iterable_obj)

# def mult(t):
#     return t * 2

# lst1 = [2, 8, 12, -5, -10]
# lst2 = list(map(mult, lst1))
# print(lst2) # [4, 16, 24, -10, -20]

# print(list(map((lambda t: t * 2), lst1))) # [4, 16, 24, -10, -20]

##############################
# t = (2.88, -1.75, 100.55)
# t2 = tuple(map((lambda x: int(x)), t))

# print(t2)

##############################
# lst = ['1', '2', '3', '4', '5']
# print(list(map(int, lst))) # [1, 2, 3, 4, 5]

##############################
# areas = [3.4343, 5.57668, 4.22323, 7.3232, 9.23244, 10.32323232]
# res = list(map(round, areas, range(1, 7))) # [3.4, 5.58, 4.223, 7.3232, 9.23244, 10.323232]
# print(res)

##############################
# lst = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]

# print(list(map((lambda x, y: (x, y)), lst, num))) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# print(dict(list(map((lambda x, y: (x, y)), lst, num)))) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

##############################
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# print(list(map((lambda x, y: x + y), l1, l2)))

##############################
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter((lambda s: len(s) == 3), t))
# print(t2)

##############################
# b = [66, 90, 56, 78, 69, 25, 63, 49]
# res = list(filter((lambda s: s < 75), b))
# print(res)

##############################
# Задача: отфильтровать список элементов.

import random as r

# lst = []
# for i in range(10):
#     lst.append(r.randint(1, 40))
# print()
# print(lst)

# res = list(filter((lambda x: x >= 10 and x <= 20 ), lst))
# print(res)
# print()

##############################

# lst = []
# for i in range(10):
#     lst.append(r.randint(1, 100))
# print()
# print(lst)

# res = list(filter((lambda x: x % 15 == 0 ), lst))
# print(res)

##############################

# m = list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 1), range(10)) ))
# print(m)

##############################
# Задача: найти слова полиндромы.

# lst = ('madam', 'fire', 'tomato', 'book', 'kiost', 'mom')
# res = list(filter((lambda x: x[::-1] == x), lst))
# print(res) # ['madam', 'mom']

##############################

# Декоратор- это функция, которая принимает другую функцию, добавляет к ней новые взможности и 
# возвращает улучшенный вариант функции.

# def hello():
#     return 'Hello, I am func "hello"'


# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())


# super_func(hello) # Hello, I am func "super_func"
                  # Hello, I am func "hello"

##############################

# def hello():
#     return 'Hello, I am func "hello"'

# test = hello
# print(test())

##############################
# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')

#     return func_wrapper

# def func_test():
#     print('Hello, I am func.')

# test = my_decorator(func_test)
# test() # Code before
       # Hello, I am func.
       # Code after

##############################

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')

#     return func_wrapper

# @my_decorator
# def func_test():
#     print('Hello, I am func.')

# func_test() # Code before
            # Hello, I am func.
            # Code after

##############################
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#     return wrap

# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#     return wrap


# @bold
# @italic
# def hello():
#     return 'text'

# print(hello()) # <b><i>text</i></b>

##############################

# def my_decorator(func):
#     n = 0
#     def wrapper():
#         nonlocal n
#         n += 1
#         print(func())
#         print(n)
#     return wrapper

# @my_decorator
# def hello():
#     return 'hello'

# hello()# hello
# #1
# hello()# hello
# #2
# hello()# hello
# # 1

##############################

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#     return wrap

# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)

# print_full_name('Artur', 'Avetisyan') # Данные:  Artur Avetisyan
                                      # Меня зовут Artur Avetisyan


##############################

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', *args)
#         print('kwargs:', **kwargs)
#         fn(*args, **kwargs)
#     return wrap

# @args_decorator
# def function(a, b, c, study='Python'):
#     print(a, b, c, 'Изучают', study, '\n')

# function('ara', 'bbb', 'cc', study='js')

##########################################################################################
            # занятие
##########################################################################################


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError()
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError
#             return fn(*f_args, **f_kwargs)

#         return wrap
#     return wrapper



# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z

# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z

# @typed(str, str, int)
# def typed_fn3(x, y, z='Hello'):
#     return (x+y)*z

# print(typed_fn(3, 4, 5))
# print(typed_fn2('z', 'y', 'x'))
# print(typed_fn3('hello', 'world', 6))


##############################
def args_decorator(tx = None, decorator_text = ''):
    def my_decorator(func):
        def wrap(*args):
            print(decorator_text, end='')
            func()
        return wrap
    if tx is None:
        return my_decorator
    else:
        return my_decorator(tx)

@args_decorator
def hello_world(text):
    print(text)