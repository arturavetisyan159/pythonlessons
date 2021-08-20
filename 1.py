# Задача 1: написать функцию, которая будет прибавлять

def func_compute(n):

    def inner_increment(x):
        return x * n

    return inner_increment

res = func_compute(2)
print(res(10))
print(res(20))

res = func_compute(3)
print(res(15))
print(res(20))
