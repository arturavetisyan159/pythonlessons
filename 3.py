# положительные элементы в начало списка

import random
my_list = []
sum = 0
for i in range(1, 11):
    my_list.append(random.randint(0, 100))
print(my_list)
my_list.sort(reverse=True)
print(my_list)