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
# Задача:

# my_str = 'Test string for me'
# print()
# def asci_code_list_converter(stroka):
#        asci_list = []
#        for el in stroka:
#               asci_list.append(ord(el))
#        return asci_list
#
# ASCII_code_list = asci_code_list_converter(my_str)
# print(f'ASCII коды: {ASCII_code_list}')
#
# sum = 0
# for elem in ASCII_code_list:
#        sum += elem
# ASCII_code_list = [int(round(sum/len(ASCII_code_list))), *ASCII_code_list]
# print(f'Среднее арифметическое: {ASCII_code_list}')
#
# new_str = input('-> ')
# new_str = new_str[0:4]
# new_code_list = asci_code_list_converter(new_str)
#
# for element in new_code_list:
#        if element in ASCII_code_list:
#               continue
#        else:
#               ASCII_code_list.append(element)
# print(ASCII_code_list)
#
# amount_of_last = 0
# for i in range(0, len(ASCII_code_list) - 1):
#        if ASCII_code_list[i] == ASCII_code_list[len(ASCII_code_list) - 1]:
#               amount_of_last += 1
#        else:
#               continue
# print(f'Количество последних элементов: {amount_of_last}')
#
# print(sorted(ASCII_code_list, reverse=True))

##############################
# print(ord('a')) # 97
# print(chr(97)) # a

##############################
# a = 122
# b = 97
# for i in range(b, a+1):
#        print(chr(i), end=' ')

##############################
# my_str = 'Test'
# sum = 0
# for el in my_str:
#        sum += ord(el)
# print(sum) # 416

##############################

s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize()) # этот метод приводит 1-ую букву в верхн. регистр, остальные в нижний "Hello, world! i am learning python."
# print(s.lower()) # переводит все буквы в нижний регистр
# print(s.upper()) # переводит все буквы в верхний регистр
# print(s.swapcase()) # переводит каждую букву строки в противоположный регистр
# print(s.title()) # переводит каждую первую букву слова в верхний регистр

# print(s.count('h')) # ищет количество символов "h"
# print(s.count('h', 1, 6)) # ищет количество символов "h" ! с 1-го индекса до 6-го(не включительно) !
# print(s.find('h')) # ищет индекс первого вхождения текущего элемента. # 0
# print(s.find('Python')) # 28
'''Если символ в s.find() не найден, выводится -1.'''
# print(s.find('Python', 0, 30)) # -1
# print(s.find('Python', 0, 40)) # 28
# print(s.index('Python')) # 28
# print(s.index('cPython')) # Выдасть ошибку, в отличие от find()
# print(s.rfind('h')) # находит последний индекс искомого элемента
# print(s.rindex('al')) # получаем тогда ошибку, в отличие от find()

# print(s.endswith('on.')) # True (заканчивается ли?)
# print(s.endswith('lo', 3, 5)) # True (от 4 до 5 не вкл.)
# print(s.endswith('lo', 3, 6)) # False

# print('abc123'.isalnum()) # True. Состоит ли строка только из букв и цифр?
# print('abc$123'.isalnum()) # False. Потому что есть еще и какой то зак $
# print('assasa'.isalpha()) # True. Состоит ли строка только из букв?
# print('12121'.isdigit()) # True. Состоит ли строка только из цифр?

# print('abc123'.isidentifier()) # True. Проверка, может ли быть идентификатором для создания переменной?
# print('123abc'.isidentifier()) # False. Потому что вначале цифры.

# print('abc'.islower()) # True. Все маленькие
# print('ab;c'.islower()) # True
# print(' '.isspace()) # True
# print('This Is A Title'.istitle()) # True

# print('aa'.center(10, '-')) # ----aa---- (весго 10 символов, аа по центру).
# print('aa'.center(2, '-')) # aa
# print('   .py'.lstrip()) # .py (обрезает пробельные символы с левой стороны)
# print('py   '.rstrip()) # .py (обрезает пробельные символы с правой стороны)
# print('https://www.python.org'.lstrip(':/pths')) # www.python.org (удалены те символы, что встретились в аргументе)
# print('py.$$;'.rstrip('$;.')) # py
# print('https://www.python.org'.lstrip(':/htps').rstrip('.org')) # www.python
# print(' www.python.org/ '.strip(' /org.w')) # python (удаляет сразу с двух сторон )

# st = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# print(st.replace('Nuthon', 'Python'))

# print('-'.join(('a', 'b', 'c'))) # a-b-c (join - приниает разделитель для кортежика и выводит в строку)
# print(':'.join('Hello')) # H:e:l:l:o (строка тоже итерируемая)
# print('Строка разделенная пробелами'.split()) # ['Строка', 'разделенная', 'пробелами'] - разделяет по пробелам и создает список
# print('Строка разделенная пробелами'.split(' ', 1)) # ['Строка', 'разделенная пробелами']



##############################
# Задача: поменять местами два слова, написанные через пробел

# s = input('Введите два слова через пробел: ')
# space = s.find(' ')
# s2 = s[space+1:len(s)]
# s1 = s[0:space]
# print(s2 + ' ' + s1)

##############################
# Задача: добавить в список все цифры в строке.

# s = 'ab12c59p7dq'
# nums = [str(i) for i in range(0, 10)]
# digits = []
# for el in s:
#        if el in nums:
#               digits.append(int(el))
# print(digits)

##############################
# s = 'hello, WORLD! I am learning Python.'
# print(s.index('Python')) # 28
# print(s.index('cPython')) # Выдасть ошибку

##############################
# Задача: вывести то, что между скобочек
# test = 'Дана ст(рока символов, среди которыхх есть одна открыв)ающаяся'
# print(test[test.index('(') + 1: test.index(')')])

##############################
# s = input('-> ')
# if s.count('f') == 1:
#        print(s.find('f'))
# elif s.count('f') == 0:
#        print('буквы f в строке нет')
# else:
#        print(s.find('f'), s.rfind('f'))

##############################
# s = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# print(s.replace('Nuthon', 'Python', 2)) # Заменяет только два раза

##############################
# my_str = 'Замените в этой строке все появления буквы \'о\' на букву \'О\', кроме первого и последнего вхождения'
# first = my_str.find('о')
# last = my_str.rfind('о')
# my_str = my_str[0:first + 1] + my_str[first + 1:last].replace('о', 'О') + my_str[last:]
# print(my_str)

##############################
# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq)) # a-b-c (join - приниает разделитель для кортежика и выводит в строку)
#
# print(':'.join('Hello')) # H:e:l:l:o (строка тоже итерируемая)

# print('Строка разделенная пробелами'.split()) # ['Строка', 'разделенная', 'пробелами']

##############################
# a = list(map(int, input('-> ').split()))
# print(a) # [2, 3, 1, 2]

##############################
# Задача: вывести фамилию и инициалы
# a = input('Введите ФИО: ').split()
# print(a[0], end=' ')
# for i in range(1, len(a)):
#     print(a[i][0] + '.', end=' ')

##############################
# a = input('Введите строку: ').split()
# print('*'.join(a))

##############################
#                                               Регулярные выражения
##############################
import re

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = 'я'
#
# print(re.findall(reg, s)) # ['я', 'я'] (reg - что мы ищем, s - где мы ищем)
#
# reg = 'совпадения'
# print(re.search(reg, s)) # <re.Match object; span=(6, 16), match='совпадения'> - с 6 по 16 элемент найден
# print(re.search(reg, s).span()) # (6, 16)
# print(re.search(reg, s).start()) # 6
# print(re.search(reg, s).end()) # 16
#
# print(re.match(reg, s)) # None (потому что производит поиск только в начале строки)
#
# reg = 'Я ищу'
# print(re.match(reg, s)) # <re.Match object; span=(0, 5), match='Я ищу'>

s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта.'
reg = 'я'
print(re.split(reg, s)) # ['Я ищу совпадени', ' в 2021 году. И ', ' их найду в 2 счёта.']

reg = '\.'
print(re.split(reg, s)) # ['Я ищу совпадения в 2021 году', ' И я их найду в 2 счёта', '']   \. , потому что точка служебный символ

