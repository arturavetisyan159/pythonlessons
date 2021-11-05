# Декоратор со степенью

class Power:
    def __init__(self, arg):
        self.power = arg

    def __call__(self, func1):
        def wrap(a, b):
            res = func1(a, b) ** self.power
            print(res)
        return wrap


@Power(3)
def func(a, b):
    return a * b

func(2, 3)
