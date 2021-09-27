import re

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
# reg = 'я'
# print(re.findall(reg, s)) # возвращает список, содержащий все совпадения
# # ['я', 'я']

# reg = 'совпадения'
# print(re.search(reg, s)) # возвращает местоположение перовго совпадения объекта
# # <re.Match object; span=(6, 16), match='совпадения'>

# reg = 'Я ищу'
# print(re.match(reg, s)) # Предназначен для поиска по заданному шаблону в начале строки
# # <re.Match object; span=(0, 5), match='Я ищу'>

# reg = r'\.'
# print(re.split(reg, s)) # возвращает список в котором строка разбита по шаблону
# # ['Я ищу совпадения в 2021 году', ' И я их найду в 2 счета', '']

# reg = r'\.'
# print(re.sub(reg, "!", s)) # Заменяет совпадения указанным текстом
# # Я ищу совпадения в 2021 году! И я их найду в 2 счета!


# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
# reg = '[201]' # чтобы множественно найти
# print(re.findall(reg, s)) # ['2', '0', '2', '1', '2']

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
# reg = '[0-9][0-9]'
# print(re.findall(reg, s))  # ['20', '21']

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = '[А-Яёа-яё]'
# print(re.findall(reg, s)) # ['Я', 'и', 'щ', 'у', 'с', 'о', 'в', 'п', 'а', 'д', 'е', 'н', 'и', 'я', 'в', 'г', 'о', 'д', 'у', 'И', 'я', 'и', 'х', 'н', 'а', 'й', 'д', 'у', 'в', 'с', 'ч', 'ё', 'т', 'а']

# s = "Петр, Ольга и Виталий отлично учатся"
# reg = r'Петр|Ольга|Виталий'
# print(re.findall(reg, s)) # 

# s = "Word2016, PS6, AI5"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I).group()) # 


# s = '5 + 7-2 - 4'
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))


############# РАБОТА С ФАЙЛАМИ

# f = open(r"text.txt", "r")
# print(f.read(7)) # Начинает чтение
# print(f.read()) # дочитывает
# f.close()


################################

# f = open(r"text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()

################################
# f = open("test.txt", "r")
# counter = len(f.readlines())
# print(counter)
# f.close()

#################################

# f = open('xyz.txt', 'w')
# print(f.write("New text.")) # 9 (количество знаков)

# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\n")

# f.close()

####################################

# f = open('text.txt', 'r')
# print(f.read(4))
# print(f.tell()) # возвращает положение курсора.
# print(f.seek(1)) # переставил курсор на 1 позицию.
# print(f.read())
# print(f.tell())
 
# f = open('text.txt', 'a')
# # print(f.write("I am learning Python")) # метод write возвращает в консоль количество символов в файле
# print(f.seek(3))
# print(f.write("-Hello-")) # удаляет и вставляет аргумент
# f.close()

######################################

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]

# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)

# with open(file_name, 'w') as f:
#     f.write(get_line(lst))

# print("Done!")

##################################

# file_name = 'res_1.txt'
# res_list = []

# def count(st):
#     return (len(st.split()), st.split())
# with open(file_name, 'r') as f:
#     line = f.read()
#     print(count(line)[0], '\n', list(map(float, count(line)[1])))

######################################

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"

# with open('one.txt', 'w', encoding='utf-8') as f:
#     f.write(text)

# read_file = "one.txt"
# write_file = "two.txt"

# with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия-")
#         fw.write(line)

###############################

# def words_list_maker(st):
#     resWordList = []
#     st = st.split(' ')
#     for s in st:
#         if s.find(',') != -1:
#             s = s.replace(',', '')
#         if s.find('.') != -1:
#             s = s.replace('.', '')
#         if s.find('-') != -1:
#             s = s.replace('-', '')
#         if s.find('?') != -1:
#             s = s.replace('?', '')
#         if s.find('!') != -1:
#             s = s.replace('!', '')
#         if s.isalpha() == True:
#             resWordList.append(s)

#     res = []

#     max = len(resWordList[0])
#     for el in resWordList:
#         if len(el) > max:
#             max = len(el)
#     for element in resWordList:
#         if len(element) == max:
#             res.append(element)
    
#     if len(res) == 1:
#         return res[0]
#     else:
#         return res

# with open('one.txt', 'r', encoding='utf-8') as f:
#     string = f.read()
#     print(words_list_maker(string))


import os
# print(os.getcwd()) # показывает директорию нашего файла
# print(os.listdir()) # получаем список файлов в текущей директории.

# print(os.listdir('..'))

# os.mkdir('folder') # создаст папку folder

# os.makedirs("nested1/nested2/nested3") # создает такую вложенность из нескольких папок

# os.remove('text.txt') # удаляет из текущего проекты файл

# os.rename('nested1', "test1") # Переименовывает папку.

os.rename('res_1.txt', 'test1/test.txt') # ПЕРЕИМЕНОВЫВАЯ, переносит в папку.
