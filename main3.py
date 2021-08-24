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
from typing import Type

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

##############################

# def args_decorator(fn):
#        def wrap(*args, **kwargs):
#               print('args:', args)
#               print('Kwargs:', kwargs)
#               fn(*args, **kwargs)
#        return wrap

# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#        print(a, b, c, 'изучают', study, '\n')

# print_full_name('Борис', 'Елизавета', 'Светлана', study='Javascript')
# print_full_name('Борис', 'Елизавета', 'Светлана')

##############################
# def args_decorator(arg1, arg2):
#        print('Я создаю декоратор! Аргументы декоратора:', arg1, arg2)

#        def my_decorator(func):
#               print('Я декоратор. Аргументы:', arg1, arg2)

#               def wrap(func_arg1, func_arg2):
#                      print('Обертка')
#                      func(func_arg1, func_arg2)
#               return wrap

#        return my_decorator

# @args_decorator('Игорь', 'Нефедов')
# def print_full_name(first, last):
#        print('Меня зовут', first, last)

# print_full_name('Artur', 'Avetisyan')

##############################

# def args_decorator(decorator_text):
#        def my_decorator(func):
#               def wrap(*args):
#                      print(decorator_text, end='')
#                      func(*args)
#               return wrap
#        return my_decorator

# @args_decorator(decorator_text='Hello, ')
# def hello_world(text):
#        print(text)

# hello_world('world!')

##############################

# def typed(*args, **kwargs):                          
#        def wrapper(fn):
#               def wrap(*f_args, **f_kwargs):
#                      for i in range(0, len(args)):
#                             if type(f_args[i]) != args[i]:
#                                    raise TypeError()
#                      for j in kwargs:
#                             if type(f_kwargs) != kwargs[j]:
#                                    raise TypeError()
#                      return fn(*f_args, **f_kwargs)     
#               return wrap
#        return wrapper


# @typed(int, int, int)
# def typed_fn(x, y, z):
       
#        return x * y * z

# @typed(str, str, str)
# def typed_fn2(x, y, z):
#        return x + y + z

# @typed(str, str, int)
# def typed_fn3(x, y, z='Hello!'):
#        return (x + y) * z

# print(typed_fn(3, 4, 5))
# print(typed_fn2('he', 'ss', 'f'))
# print(typed_fn3('Hey', 'Arnold', z=5))

##############################

# def args_decorator(tx=None, decorator_text=''):
#        def my_decorator(func):
#               def wrap(*args):
#                      print(decorator_text, end='')
#                      func(*args)
#               return wrap
#        if tx is None:
#               return my_decorator
#        else:
#               return my_decorator(tx)

# @args_decorator
# def hello_world(text):
#        print(text)

# @args_decorator(decorator_text='Hello, ')
# def hello_world2(text):
#        print(text)

# hello_world('HI')
# hello_world2('World')

##############################
# print(bin(19)) # 0b10011
# print(oct(19)) # 0o23
# print(hex(19)) # 0x13

# # Двоичная СИ: 0b или 0B
# print(0b1010) # 10

# # Восьмеричная СИ - 0o или 0O
# print(0o12) # 10

# # Шестнадцатиричная - 0x или 0X
# print(0xFF)

# s = 'Hello'
# print(s[4:0:-2]) # ol

##############################
# s = 'abcdefgh'
# print(s[slice(7, None, -1)]) # hgfedcba

##############################
# s = 'Python'
# s = s[:3] + 't' + s[4:]
# print(s)

##############################
# str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык.'
# def change(stroka, symbol1, symbol2):
#        for l in range(0, len(stroka)):
#               if stroka[l] == symbol1:
#                      stroka = stroka[:l] + symbol2 + stroka[l+1:]
              
#        return stroka
# print(change(str1, 'N', 'P')) # Я изучаю Puthon. Мне нравится Puthon. Puthon очень интересный язык.

##############################

# import math as m

# print('C:\\file.txt') # C:\file.txt
# # префикс 'r' перед строкой отменяет экранирование.
# print(r'C:\D') # C:\D

# # префикс 'b'
# print(b'a1b2c3'[1]) # 49

# # префикс 'f' позволяет спокойно использовать переменные в выводе
# name = 'Дмитрий'
# age = 25
# print(f'{name}') # Дмиртрий

# Префикс 'fr'- объединение 'f' и 'r'
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}') # home\my_doc\data.txt

##############################
# def square(n):
#        '''Функция которая возводит в квадрат принимаемое число n. Возвращает его квадрат'''
#        return n**2
# print(square(5))

##############################
# print(ord('a')) # 97

##############################
my_str = 'Test string for me'
print()
def asci_code_list_converter(stroka):
       asci_list = []
       for el in stroka:
              asci_list.append(ord(el))
       return asci_list

ASCII_code_list = asci_code_list_converter(my_str)
print(f'ASCII коды: {ASCII_code_list}')

sum = 0
for elem in ASCII_code_list:
       sum += elem
ASCII_code_list = [int(round(sum/len(ASCII_code_list))), *ASCII_code_list]
print(f'Среднее арифметическое: {ASCII_code_list}')

new_str = input('-> ')
new_str = new_str[0:4]
new_code_list = asci_code_list_converter(new_str)

for element in new_code_list:
       if element in ASCII_code_list:
              continue
       else:
              ASCII_code_list.append(element)
print(ASCII_code_list)

amount_of_last = 0
for i in range(0, len(ASCII_code_list) - 1):
       if ASCII_code_list[i] == ASCII_code_list[len(ASCII_code_list) - 1]:
              amount_of_last += 1
       else:
              continue
print(f'Количество последних элементов: {amount_of_last}')

print(sorted(ASCII_code_list, reverse=True))

