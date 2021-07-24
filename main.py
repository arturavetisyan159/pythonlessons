import random as r
import math
import time
import locale
locale.setlocale(locale.LC_ALL, "ru_RU")


# работа с оператором print

# name = str(input('What is yor name? '))
# age = int(input('How old are u? '))
# print('My name is', name + '. I am', str(age), 'years old.', sep=" ", end=" ")
# print("Новая строка")


# %s = string. %d = digital. %.2f = float(2 символа после запятой)

# name = "Viktor"
# age = 28
# grade = 9.2
# print("It is %s, %d. Level: %.3f" % (name, age, grade))


# метод .format

# print("This is a {0}. It is {1}".format("ball", "red"))


# задача

# print("Введите 4 числа: ")
# frst = int(input("1: "))
# scnd = int(input("2: "))
# thrd = int(input("3: "))
# frth = int(input("4: "))

# res1 = frst + scnd
# res2 = thrd+ frth
# result = res1 / res2
# print("Ваш ответ: %.2f" % (result))


# bool

# test = None
# print(test is None) # true


# a = 1
# b = 2

# a,b = 2,1
# print(a,b)

# a = 1
# b = 2
#
# a = b
# b = 1
# print(a,b)

# double_letter = [letter * 2 for letter in 'Banana']
# print(double_letter)

# b = list(range(1, 10))
# print(b) # [1 2 3 4 5 6 7 8 9]

# a = [0 for i in range(5)]
# print(a) # [0, 0, 0, 0, 0]

# my_list = [int(input("%d-ый элемент: " % (i+1))) for i in range(int(input("Введите количество элементов списка: ")))]
# print(my_list)

# список[start:stop:step]

##############################
# МАТРИЦЫ
##############################

# задача: остсортировать четные строки матрицы по возраст. , а нечетные по убыванию

# mas = [[2, 5, 8],
#        [5, 8, 2],
#        [8, 7, 1],
#        [0, 7, 1],
#        [9, 11, 6]]

# for i in range(0, len(mas)):
#     if i % 2 == 0 or i == 0:
#         mas[i].sort()
#     else:
#         mas[i].sort(reverse=True)

# for row in mas:
#     for m in row:
#         print(m, end='\t')
#     print()

# наполнить список n рандомными элементами

# n = int(input("размер списка: "))
# my_list = []
# for i in range(0, n):
#     my_list.append(random.randrange(0, 21))
# print(my_list)



# w, h = 3, 4
# matrix = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# multiply = 1
# for row in matrix:
#     for w in row:
#         if w > 0:
#             multiply *= w
#         print(w, end='\t')
#     print()
# print('Произведение ненулевых элементов =', multiply)


# Задача: составить список из элементов главной диагонали

# w = int(input("Размерность массива: "))
# h = w
# print("Массив из случайных чисел от 1 до 100: ")
# matrix = [[r.randint(1, 101) for x in range(h)] for y in range(h)]
# my_list = []

# for row in matrix:
#     for j in row:
#         print(j, end='\t')
#     print()
#
# for i in range(0, w):
#     my_list.append(matrix[i][i])
# print(my_list)

# Задача: поменять местами 1-ую и 2-ую, 3-ую и 4-ую, 5-ую и 6-ую.
# w, h = 6, 6
# matrix = [[r.randint(1, 10) for x in range(w)] for y in range(h)]

# for row in matrix:
#     for j in row:
#         print(j, end='\t')
#     print()
#
# print()

# for h in range(len(matrix)):
#     if h % 2 == 0 and h != len(matrix):
#         for w in range(len(matrix[h])):
#             print(matrix[h + 1][w], end='\t')
#         print()
#         for w in range(len(matrix[h])):
#             print(matrix[h][w], end='\t')
#         print()


# Задача: вывести матрицу рабочих дней.

# days = [d for d in range(1, 32)]
#
# weeks = [days[i: i + 7]for i in range(0, len(days), 7)]

# work_weeks = [week[0:5] for week in weeks]
#
# for row in work_weeks:
#     for x in row:
#         print(x, end='\t')
#     print()


# Задача: наполнить список n УНИКАЛЬНЫМИ рандомными элементами

# n = int(input("Размерность списка: "))
# my_list = []
# while n != len(my_list):
#     new_element = r.randint(1, n)
#     if new_element not in my_list:
#         my_list.append(new_element)
# print(my_list)

##############################
# MATH
##############################

# num1 = math.sqrt(6)
# num2 = math.ceil(3.3)
# num3 = math.floor(3.8)
# print('округление в большую сторону:', num2)
# print('округление в меньшую сторону:', num3)

# a, b = 13, 26
# print("Наибольший общий делитель:", math.gcd(a, b))

# num_list = [21, 3, 3, 4, 4]
# print("Сумма элемнтов списка:", int(math.fsum(num_list)))

######################
# TIME
######################

# seconds = time.time()
# print("Секунды с начала эпохи: ", seconds)

# local_time = time.ctime(seconds)
# print("местное время: ", local_time)

# res = time.localtime(seconds)
# print("Local time:", res)
# print("Год:", res.tm_year)

# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
#
# pause = 5
# print("Programm started..")
# time.sleep(pause)
# print("finish")

# remind_text = input("Название напоминания: ")
# timing = int(input("Через сколько секунд? "))
# pause = time.sleep(timing)
# print(remind_text)

# start1 = time.monotonic()
# time.sleep(5)
# result = time.monotonic() - start1
# print(result)


# print(time.strftime("Сегодня: %d %B, %Y."))

# from decimal import Decimal, ROUND_HALF_UP
#
# num = Decimal("10.0055")
# num = num.quantize(Decimal("1.00"), ROUND_HALF_UP)
# print(num)

######################
# ФУНКЦИИ
######################

# def queue_line(frst, scnd, quant):
#     for i in range(1, quant + 1):
#         if i % 2 == 0:
#             print(scnd, end=' ')
#         else:
#             print(frst, end=' ')
# queue_line('(', ')', 10)


######################
# def maximum(x, y):
#     if x > y:
#         return (x - y)
#     else:
#         return x + y
#
# a = int(input("a = "))
# b = int(input("b = "))
#
# print("Результат:", maximum(a, b))

# ######################

# def triple(num):
#     return num**3
#
# for i in range(1, 11):
#     print(i, "в кубе =", triple(i))

# ######################
# def change_elements(lst):
#     first = lst[0]
#     last = lst[len(lst) - 1]
#     lst[0] = last
#     lst[len(lst) - 1] = first
#     return lst
# print(change_elements([1, 2, 2, 3, 4, 5 ,6]))
# print(change_elements(['c', 'л', 'о', 'н']))

#######################
# def queue(num = 20, symb = '-'):
#     return(symb * num)
# print(queue(10, symb = '+'))
# print(queue(20, "/"))

#######################
# def check_password(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#     elif check_username and username in password:
#         print("Пароль содержит имя пользвателя")
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки")
#         return True
# check_password('Artur', '12112', 5)

#########################

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

#########################

# def func(a, ln=[]):
#     ln.append(a)
#     return ln
#
# print(func(1))
# print(func(2))
# print(func(3))
#
# print()
#
# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
# print(func(1))
# print(func(2))
# print(func(3))

#########################

# lt1 = [1, 2, 3] # id = 4444184832
# lt2 = [1, 2, 3] # id = 4443586944
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2) # True
# print(lt2 is lt1) # False

########################

# lt1 = [1, 2, 3]
# lt2 = lt1
# print(id(lt1)) # 4488167680
# print(id(lt2)) # 4488167680
# lt2.append(1)
# print(id(lt2)) # 4488167680
# print(lt1) # [1, 2, 3, 1]

########################
# s = "Hello"
# print(id(s)) # 4550074672
# s = "ada;d"
# print(id(s)) # 4550074736

##############################
# a = "h"
# b = "h"
# print(id(a), id(b))

##############################
# a = [1, 2, 3]
# print(id(a))
# # a = a + [4, 5] # id будут разные в итоге
# # a += [4, 5] # id будут одинаковые в итоге, то есть += и = ... + ..., хранятся в памяти совершенно по разному.
# print(id(a))

##############################
# def add_number(n):
#     print("Внутри функции", n, "=", id(n))
#     n += 1
#     print("После присвоения", n, "=", id(n))
#
# x = 1
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

##############################
# КОРТЕЖ (tuple)
##############################

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__()) # 104
# print(tpl.__sizeof__()) # 48

##############################
# a = (1, 2, 3, 4, 5)
# print(a)
# b = 1, 2, 3
# print(type(b))
# print(b)

##############################
# t = (1)
# print(type(t)) # int
#
# t = (1,)
# print(type(t)) # tuple
#
# t1 = tuple('hello')
# print(t1) # ('h', 'e', 'l', 'l', 'o')
# print(t1[1:3])

##############################
# s1 = tuple([int(input('-> ')) for i in range(0, 5)])
# print(s1)

##############################
# s = input("-> ")
# a = tuple(s)
# print(a)

##############################
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas) # [94, 58, 77, 37, 28, 44, 89, 10, 74, 23]
# tp1 = tuple(mas) # (94, 58, 77, 37, 28, 44, 89, 10, 74, 23)
# print(tp1)

##############################
# Заполнить кортеж степенями двойки от 1 до 12
# tp1 = tuple([2**i for i in range(1, 13)])
# print(tp1)

##############################
# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# print(len(t3)) # 11
# print(t3.count('l')) # 3
# print(t3.count('a')) # 0
# print(t3.index('l')) # 2
#
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('Такого символа нет')

##############################
# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# for i in t3:
#     if i == ' ':
#         continue
#     print(i, end=' ')

##############################
# Срез кортежей
# def slicer(tpl, el):
#     tpl_new = list(tpl)
#     lst = []
#     if tpl.count(el) == 0:
#         return tuple(())
#     elif tpl.count(el) == 1:
#         tpl_new = tpl_new[tpl_new.index(el):len(tpl_new)]
#         tpl_new = tuple(tpl_new)
#         return tpl_new
#     else:
#         tpl_new = tpl_new[tpl_new.index(el):len(tpl_new)]
#         ind = 0
#         for i in range(1, len(tpl_new)):
#             if tpl_new[i] == el:
#                 ind = i
#         tpl_new = tpl_new[0:ind]
#         return tuple(tpl_new)
#
# print(slicer((1,2,3), 8))
# print(slicer((1,8,3,4,8,8,9), 8))
# print(slicer((1,2,8,5,1,2,9), 8))

##############################
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first_index = tpl.index(el)
#             second_index = tpl.index(el, first_index + 1) # !!! INDEX(ИНДЕКС ИСКОМОГО ЭЛ, СТАРТОВАЯ П-ИЯ ОТСЧЕТА) !!!
#             return tpl[first_index:second_index + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return ()
#
#
# print(slicer((1,2,3), 8))
# print(slicer((1,8,3,4,8,8,9), 8))
# print(slicer((1,2,8,5,1,2,9), 8))

##############################
# Наполнить кортеж элементами

# tpl1 = tuple([r.randint(0, 5) for i in range(10)])
# print(tpl1)
# tpl2 = tuple([r.randint(-5, 0) for i in range(10)])
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
#
# def count(tpl):
#     counter = 0
#     for el in tpl:
#         if el == 0:
#             counter += 1
#     return counter
#
# print('Количество нулей в 3 кортеже :', count(tpl3))

##############################
# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t)

##############################
# развернуть и найти уникалные элементы
# def tuple_convert(lst):
#     new_lst = []
#     for i in range(len(lst) - 1, -1, -1):
#         if lst[i] in new_lst:
#             continue
#         else:
#             new_lst.append(lst[i])
#     tpl = tuple(new_lst)
#     return tpl
#
# print(tuple_convert([1, 2, 3, 3, 2]))
# print(tuple_convert([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))