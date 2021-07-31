# Задание 4: написать функцию нахожд минимального значения произвольного количества элементов
def minValue(*args):
    min = args[0]
    for el in args:
        if el < min:
            min = el
    return min

print(minValue(9, 10))
print(minValue(2, 3, 4))
print(minValue(3, 5, 10, 6))
