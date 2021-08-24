# Задача 4: написать функцию перевода десятичного числа в двоичное.
def binary_convert(num):
    deg = 2
    i = 0
    while num <= deg:
        deg = 2**i
        i += 1
    print(i)

binary_convert(29)

