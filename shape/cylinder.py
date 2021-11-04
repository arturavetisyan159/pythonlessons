from shape.rectangle import Rectangle
from shape.circle import Circle


class Cylinder(Circle, Rectangle):
    def __init__(self, r, h):
        Circle.__init__(self, r)
        Rectangle.__init__(self, self.get_circle_circumference(), h)

    def get_volume(self):
        res = self.get_circle_square() * self.h
        print(f"Объем равен: {self.get_circle_square() * self.h}")
        return res
    
    def print_cylinder(self):
        print(f"Основание: {self.r}, высота: {self.h}")

