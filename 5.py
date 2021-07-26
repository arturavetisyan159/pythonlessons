# Задание 4: олимпиады по физике и математике

all_winners = ['Natalia', 'Maxim', 'Evgeniya', 'Alexandr', 'Matvey', 'Mikhail']
print('Все призеры:', all_winners)

math = ['Matvey', 'Evgeniya', 'Mikhail', 'Maxim', 'Natalia']
physics = ['Maxim', 'Matvey', 'Alexandr']

math = set(math)
math.intersection_update(physics)
print('Призеры обеих олимпиад:', math)
print('Обновленный список призеров по олимпиаде:', math)
