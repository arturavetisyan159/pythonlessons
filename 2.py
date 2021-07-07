# сумма элемнтов списка

import random
my_list = []
sum = 0
for i in range(1, 21):
    my_list.append(random.randint(1, 100))
print(my_list)
for el in my_list:
    sum = sum + el
print("Сумма элементов списка:", sum)