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
# f = open("test2.txt", "r")
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

#####################################

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

# os.rename('test1/test2.txt', 'test1/new/test2.txt') # ПЕРЕИМЕНОВЫВАЯ, переносит в папку.

# os.rmdir("folder") # Удаляет папку "folder"

# os.walk(folder_name, topdown=True) # Идет по дереву сверху вниз или снизу вверх и выводит название корневой папки, список подпапок и список файлов

# for root, dirs, file in os.walk('test1', topdown=True):
#     print("Root", root)
#     print("Subdirs", dirs)
#     print("Files", file)

# for root, dirs, file in os.walk('test1', topdown=True):
#     if len(os.listdir(root)) == 0:
#         os.rmdir(root)
#         print('Директория', root, "была удалена.")

import os.path
# print(os.path.split(r"C:\Users\Артур Аветисян\Desktop\pythonlessons\test1\new\test2.txt")) # split разделяет на кортежи - в первый кортеж- все что жо последнего слеша, во второй - то что после последнего слеша.
# print(os.path.dirname(r"C:\Users\Артур Аветисян\Desktop\pythonlessons\test1\new\test2.txt")) # возвращает первй кортеж
# print(os.path.basename(r'C:\Users\Артур Аветисян\Desktop\pythonlessons\test1\new\test2.txt')) # возвращает второй кортеж

# print(os.path.join(r"C:\Users\Артур Аветисян\Desktop\pythonlessons\test1", 'new')) # просто совмщает в один путь, добавляя слешы.

###########################
# Задание.

# dirs = ["Work/F1", "Work/F2/F21"]
# for i in dirs:
#     os.makedirs(i)

# files = {
#     "Work": ["w.txt"],
#     "Work/F1": ["f11.txt", "f12.txt", "f13.txt"],
#     "Work/F2/F21": ["F211.txt", "F212.txt"]
# }
# for i, files in files.items():
#     for file in files:
#         file_path = os.path.join(i, file)
#         open(file_path, "w").write(file_path)
# print("Cверху вниз")
# for direct, folder, file in os.walk("Work"):
#     print(direct, folder, file)
# print("Снизу вверх")
# for direct, folder, file in os.walk("Work", topdown=False):
#     print(direct, folder, file)

#######################
# ДЗ задание 1.

# res_list = []

# for dir, folders, files in os.walk("Work"):
#     for direction in folders:
#         res_list.append(f"{dir}//{direction}")
#     for file in files:
#         res_list.append(f"{dir}//{file}")
#     break
# print(res_list)

#########################

#print(os.path.exists(r"C:\Users\Артур Аветисян\Desktop\pythonlessons\Work\w.txt"))

#########################
# import time

# file_path = r"Work/F2/F21/F211.txt"

# if os.path.exists(file_path):
#     print("Файл существует.")
#     print(f"Файл называется - {os.path.split(file_path)[1]}")
#     print(f"Директория файла: {os.path.split(os.path.split(file_path)[0])[1]}")
#     atime = os.path.getatime(file_path)
#     print("Последний доступ к файлу:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))

# else:
#     print("Такого файла не существет!")

###########################
print(os.path.normcase('C:/User/admin/Documents'))
