# объеденить в третьем первый и второй файлы

first = ''
second = ''

with open('task21.txt', 'r', encoding='utf-8') as fr1:
    first = fr1.read()

with open('task22.txt', 'r', encoding='utf-8') as fr2:
    second = fr2.read()

with open('task23.txt', 'w', encoding='utf-8') as fw:
    fw.write(first + second)
