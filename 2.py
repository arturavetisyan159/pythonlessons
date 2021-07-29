# ЗАДАНИЕ 2: поменять ЗП

d = {
    'emp1': {
        'name': 'John',
        'salary': 7500
    },
    'emp2': {
        'name': 'Emma',
        'salary': 8000
    },
    'emp3': {
        'name': 'Brad',
        'salary': 6500
    }
}

print(d['emp3'])
d['emp3']['salary'] = 8500

print('Зарплата Брэда изменена с 6500 на 8500')

for x in d:
    print()
    print(x, ':', sep='')
    for y in d[x]:
        print(y, ':', ' ', d[x][y], sep='')
