# Задача 2: преобразовать посл-ость чисел.
lst1 = [3, 6, 8, 9, 1, 2]
lst2 = list(map((lambda x: x * lst1.index(x)**3), lst1))

print(lst2)

