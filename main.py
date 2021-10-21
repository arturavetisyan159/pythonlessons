# Класс Pair
import math as m

class Pair:
    def __init__(self, a, b):
        if self.check_numbers(a, b):
            self.a = a
            self.b = b
        else:
            raise ValueError("Ошибка. числа должны быть типа integer")
    
    def change_numbers(self, a, b):
        if self.check_numbers(a, b):
            self.a = a
            self.b = b

    @staticmethod
    def check_numbers(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        return False

    def sum_numbers(self):
        res = self.a + self.b
        print(f"Сумма = {res}")
        return res

    def multiply_numbers(self):
        res = self.a * self.b
        print(f"Произведение = {res}")
        return res


class RightTriangle(Pair):
    def hypotenuse(self):
        res = round(m.sqrt(self.a**2 + self.b**2), 2)
        print(f"Гипотенуза треугольника = {res}")
        return res

    def square(self):
        res = (self.a * self.b) / 2
        print(f"Площадь треугольника = {res}")
        return res

    def info(self):
        print(f"Прямоугольный треугольник ABC ({self.a}, {self.b}, {self.hypotenuse()})")


tr1 = RightTriangle(5, 8)
tr1.info()
tr1.square()
print()
tr1.sum_numbers()
tr1.multiply_numbers()



