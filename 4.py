# Элементы с нечетным индексом

my_list = []

n = int(input("n= "))

for i in range(1, n + 1):
    a = int(input("=> "))
    my_list.append(a)

for j in range(0, n):
    if j % 2 == 0:
        print(my_list[j], end=" ")
    else:
        continue
