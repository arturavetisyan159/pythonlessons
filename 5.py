# Вывд элементов, которые больше предыдущих

my_list = []

n = int(input("n= "))

for i in range(1, n + 1):
    a = int(input("=> "))
    my_list.append(a)

for j in range(1, n):
    if my_list[j] > my_list[j-1]:
        print(my_list[j], end=" ")
    else:
        continue
