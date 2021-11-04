# Класс Rectangle

class Rectangle:
    def __init__(self, l, h):
        self.l= l
        self.h = h

    def get_rect_perimeter(self):
        res = (self.l + self.h) * 2
        print(f"Периметр равен: {(self.l + self.h) * 2}")
        return res

    def get_rect_area(self):
        res = self.l * self.h
        print(f"Площадь прямоугольника: {self.l * self.h}")
        return res

    def print_rect(self):
        print(f"Стороны : {self.l} , {self.h}")
