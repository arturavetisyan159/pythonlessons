# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1

# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# p1 = Point()
# p1.x = 1100
# print(p1.x, p1.y) # 1100 1
# print(getattr(Point, "x")) # 1
# print(getattr(p1, "x")) # 1100
# print(getattr(p1, "z", "Такого атрибута нет")) # Такого атрибута нет"
# print(hasattr(p1, "x")) # True
# setattr(p1, "z", 7)
# print(p1.__dict__)

# print(isinstance(p1, Point)) # True (принадлежит ли экземпляр к этому классу)


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Point()
# p1.set_coords(5, 10)
# # Можно сделать вот так:
# Point.set_coords(p1, 3, 1)

# p2 = Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.qual = 0
    
    def info(self):
        print("Информация:", self.name, self.surname)

    def quality(self, point):
        self.qual = self.qual + point
        print("Квалификация:", self.qual)

first_person  = Person("Артур", "Аветисян")
first_person.info()
first_person.quality(2)
first_person.quality(1)
