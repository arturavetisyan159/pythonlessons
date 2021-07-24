# Задание 1 - наибольшое положительное число кортежа кратное 13

tpl1 = 2, 7, 0, 3, 1, 5, -13
tpl2 = 2, 7, 0, 3, 1, 5, -13, 13
tpl3 = (26,)
tpl4 = 99, 99, 100, 34, -39
tpl5 = 99, 39, 99, 100, 34

def div_13(tpl):
    new_tpl = []
    max = 'no such numbers'
    for el in tpl:
        if el > 0 and el % 13 == 0:
            new_tpl.append(el)
            max = el
    for element in new_tpl:
        if element > max:
            max = element
    return max

print(div_13(tpl1))
print(div_13(tpl2))
print(div_13(tpl3))
print(div_13(tpl4))
print(div_13(tpl5))
