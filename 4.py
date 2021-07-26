# Задание 4: найти все зависимости двух множеств

def sets(set1, set2):
    print('Union:', set1.union(set2))
    print('Intersection:', set1.intersection(set2))
    print('Symmetric difference:', set1.symmetric_difference(set2))
    print('s2 unique elements:', set1 - set2)
    print('s2 is superset for {4, 5, 7}:', set2.issuperset({4, 5, 7}))
    print('s2 is superset for {8, 4, 3}:', set2.issuperset({8, 4, 3}))
    print('s2 is right superset for {4, 5, 6, 7, 8}', set2 > {4, 5, 6, 7, 8})

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

print()
sets(set_1, set_2)