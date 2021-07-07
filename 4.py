# Транспозиция матрицы

import random
matrix = []
new_matrix = []
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

index = 0
for counter in range(0, (elements_in_row - 1)):
    new_matrix.append(list())
    for g in new_matrix:
        g.append(matrix[counter][index])
        index += 1


