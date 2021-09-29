pos = int(input('pos = '))
with open('task4.txt', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    res = []
    for i in range(0, len(lines)):
        if i == pos:
            continue
        res.append(lines[i])

    for j in range(0, len(res)):
        if '\n' not in res[j]:
            res[j] = res[j] + '\n'

with open('task4.txt', 'w', encoding='utf-8') as fw:
    res_str = ''
    for el in res:
        res_str += el
    fw.write(res_str)
