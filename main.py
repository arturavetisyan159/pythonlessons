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
#
# res1 = frst + scnd
# res2 = thrd+ frth
# result = res1 / res2
# print("Ваш ответ: %.2f" % (result))


# bool

# test = None
# print(test is None) # true


# a = 1
# b = 2
#
# a,b = 2,1
# print(a,b)
#
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