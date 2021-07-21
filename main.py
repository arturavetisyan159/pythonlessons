import random as r
import math
import time


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

# num1 = math.sqrt(6)
# num2 = math.ceil(3.3)
# num3 = math.floor(3.8)
# print('округление в большую сторону:', num2)
# print('округление в меньшую сторону:', num3)

# a, b = 13, 26
# print("Наибольший общий делитель:", math.gcd(a, b))

# num_list = [21, 3, 3, 4, 4]
# print("Сумма элемнтов списка:", int(math.fsum(num_list)))

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

import time
import locale
locale.setlocale(locale.LC_TIME, "Russian_Russia.65001")


print(time.strftime("Сегодня: %B %d, %Y."))