# Изменить порядок строк в файле на обратный

with open('task1.txt', 'r', encoding='utf8') as f:
    a = f.readlines()
    for i in range(0, len(a)):
        if '\n' in a[i]:
            a[i] = a[i].replace('\n', '')
    print(a)
with open('task1.txt', 'w', encoding='utf-8') as file:
    s = ''
    for j in range(len(a) - 1, -1, -1):
        if j == 0:
            s += a[j]
            continue
        line = str(a[j]) + '\n'
        s += line
    file.write(s)