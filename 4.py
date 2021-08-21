# Задача 4: удалить неотрицательные элементы, посчитать сумму и вывести абс значение.

l = [3, -4, -6, 7, -8, 3, -12, 4, 7]
sum = 0

for element in list(filter((lambda x: x < 0), l)):
    sum += abs(element)
print(sum)
