# Задание 3: создать словарь с помощбю генератора словарей

lst1 = ['color', 'fruit', 'pet']
lst2 = ['blue', 'apple', 'dog']
d = {x: y for x, y in tuple(zip(lst1, lst2))}

print(d)