s = input('Строка: ').split()
sub = input('Ее заменяемая подстрока: ')
new_sub = input('Новая подстрока: ')
new_s = []

for el in s:
    if el == sub:
        continue
    else:
        new_s.append(el)

print(new_sub.join(new_s))

