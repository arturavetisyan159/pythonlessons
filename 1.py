amount = int(input("Введите количество элементов списка: "))
first_list = []
for i in range(1, amount + 1):
    element = int(input("Введите элемент списка: "))
    first_list.append(element)
print("Ваш список:", first_list)

plus_list = []
for el in first_list:
    if el > 0:
        plus_list.append(el)
    else:
        continue
print("Список, состоящий только из положительных элементов:", plus_list)

max_element = 0
for ell in plus_list:
    if ell > max_element:
        max_element = ell
print("Максимальный элемент в списке:", max_element)
