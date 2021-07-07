# Транспозиция матрицы

import random
matrix = []
for i in range(0, 3):
    matrix.append(list())
for j in matrix:
    for k in range(0, 4):
        k = random.randint(1, 10)
        j.append(k)

for row in matrix:
    elements_in_row = len(row)
    for m in row:
        print(m, end="\t")
    print()
print()

