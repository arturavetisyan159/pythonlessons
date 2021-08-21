# Задание: создать функцию декоратор которая суммирует.

def multiply(num):
    def outer(func):
        def wrapper(arg):
            return func(arg) * num

        return wrapper
    return outer

@multiply(3)
def return_num(a):
    return a
print('Результат:',return_num(5))

