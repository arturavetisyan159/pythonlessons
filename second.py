# Задание 2: поменять местами 1-ю и 2-ую строки

f_read = open('second.txt', 'r', encoding='utf8')
lines_list = f_read.readlines()
lines_list_2 = []
for element in lines_list:
    if element.endswith('\n'):
        element = element.replace('\n', '')
        lines_list_2.append(element)
    else:
        lines_list_2.append(element)

pos1 = int(input('pos1 => '))
pos2 = int(input('pos2 => '))

first_onChange = lines_list_2[pos1-1]
lines_list_2[pos1 - 1] = lines_list_2[pos2 - 1]
lines_list_2[pos2 - 1] = first_onChange
f_read.close()

f_write = open('second.txt', 'w', encoding="utf8")
for el in lines_list_2:
    f_write.write(el + '\n')
