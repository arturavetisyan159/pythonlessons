# Задание 6: set_gen

def set_gen(lst):
    new_list = []
    for element in lst:
        if element in new_list:
            continue
        else:
            new_list.append(element)

    for el in new_list:
        if lst.count(el) >= 2:
            for i in range(2, lst.count(el) + 1):
                new_list.append(str(el) * i)
        else:
            continue
    res_set = set(new_list)
    return res_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))