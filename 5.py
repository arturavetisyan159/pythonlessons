# Задание 5: функция суммирования

def summing(*args):
    sum = 0
    res = []
    for el in args:
        sum = el + sum
        res.append(sum)
    return res

print(*summing(3, 9, 1))
print(*summing(2, 5, 4, 2))
print(*summing(3, 5, 10, 6, 3))
