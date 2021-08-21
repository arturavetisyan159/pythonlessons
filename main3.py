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

##############################
# from datetime import datetime

# def timeit(arg):
#     print(arg)
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             start = datetime.now()
#             result = func(*args, **kwargs)
#             print(datetime.now() - start)
#             return result
#         return wrapper
#     return outer

# @timeit('name')
# def one(n):
#     l = []
#     for i in range(n):
#         if i % 2 == 0:
#             l.append(i)
#     return l

# @timeit('name')
# def two(n):
#     l = [x for x in range(n) if x % 2 == 0]
#     return l

# one(10)


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
# def args_decorator(tx = None, decorator_text = ''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func()
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)

# @args_decorator
# def hello_world(text):
#     print(text)



