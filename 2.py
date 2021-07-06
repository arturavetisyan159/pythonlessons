my_list = []
new_list = []
amount = int(input("Введите количество элементов списка: "))
for i in range(1, amount + 1):
    element = int(input("=> "))
    my_list.append(element)
k = int(input("Введите индекс: "))
c = int(input("Введите значение: "))

if k > len(my_list) - 1:
    print("Слишком большой индекс.")
else:
    for j in range(0, len(my_list) + 1):
        if j < k:
            new_list.append(my_list[j])
        elif j == k:
            new_list.append(c)
        elif j > k:
            new_list.append(my_list[j - 1])
    print("Получившийся список:", new_list)
