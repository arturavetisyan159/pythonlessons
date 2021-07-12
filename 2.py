my_list = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
simple_list = []
ordinary_list = []
def is_simple(a):
    counter = 0
    for i in range(1, a + 1):
        if a % i == 0:
            counter += 1
        else:
            continue
    if counter == 1 or counter == 2:
        return True
    else:
        return False

def minimum(spisok):
    if len(spisok) == 0:
        return None
    else:
        min = spisok[0]
        for el in spisok:
            if el < min:
                min = el
            else:
                continue
        return min

def maximum(listik):
    if len(listik) == 0:
        return None
    else:
        max = listik[0]
        for el in listik:
            if el > max:
                max = el
            else:
                continue
        return max

for element in my_list:
    if is_simple(element) == True:
        simple_list.append(element)
    else:
        ordinary_list.append(element)

min_value = minimum(simple_list)
max_value = maximum(ordinary_list)

print("Min =", min_value)
print("Max =", max_value)
