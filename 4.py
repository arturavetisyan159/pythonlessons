# Задача 4: написать функцию перевода десятичного числа в двоичное.

def binary_convert(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    deg = 2
    deg_list = []
    i = 0
    while deg <= num:
        deg = 2**i
        deg_list.append(deg)
        i += 1
    amount = i - 1
    deg_list.pop()
    res_str = ''
    for j in range(amount - 1, -1, -1):
        if num >= deg_list[j]:
            res_str = res_str + '1'
            num = num - deg_list[j]
        else:
            res_str = res_str + '0'
    return res_str

number = int(input('-> '))
print(binary_convert(number))

