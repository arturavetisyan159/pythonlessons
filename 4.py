s = 'Ежевику для ежат ежевику еле-еле Ежата возле ели съели'
counter = 0

for el in s.split():
    if el[0] == 'Е' or el[0] == 'е':
        counter += 1

print('Слов с буквой \'е\':', counter)

