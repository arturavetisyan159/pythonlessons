from math import pi as pi

class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_square(self):
        res = pi * self.r ** 2 
        print(f"Площадь круга - {pi * (self.r ** 2 )}")
        return res

    def get_circle_circumference(self):
        res = 2 * pi * self.r
        print(f"Длина окружности - {2 * pi * self.r}")
        return res

    def print_circle(self): 
        return f"Радиус = {self.r}"
