# ЗАДАНИЕ 1: объеденить 3 словаря в 1

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}

d1.update(list(d2.items()))
d1.update(list(d3.items()))
print(d1)