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

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.qual = 0
    
#     def info(self):
#         print("Информация:", self.name, self.surname)

#     def quality(self, point):
#         self.qual = self.qual + point
#         print("Квалификация:", self.qual)

# first_person  = Person("Артур", "Аветисян")
# first_person.info()
# first_person.quality(2)
# first_person.quality(1)

#########################

# class Point:
#     counter = 0

#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.counter += 1

#     def __checkValue(z):
#         if (isinstance(z, int) or isinstance(z, float)):
#             return True
#         return  False
    
#     def setValue(self, x, y):
#         if Point.__checkValue(x) and Point.__checkValue(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть чсилами!")

#     def setValue_x(self, x):
#         if Point.__checkValue(x):
#             self.__x = x
#         else:
#             print("Координата должна быть числовая!")

#     def setValue_y(self, y):
#         if Point.__checkValue(y):
#             self.__y = y
#         else:
#             print("Координата должна быть числовая!")
    
#     def getValue(self):
#         return f"{self.__x}, {self.__y}"

#     def getValue_x(self):
#         return self.__x

#     def getValue_y(self):
#         return self.__y

# first = Point(5, 10)
# first.setValue(6, 15)
# print(first.getValue())

# first.setValue_x(10)
# print(first.getValue())

# print(first.getValue_x())
# print(first.getValue_y())

####################
class Rectangle:

    def __init__(self, w=0, h=0):
        self.__width = w
        self.__height = h
    
    def setValue(self, w, h):
        self.__width = w
        self.__height = h

    def getValue(self):
        return self.__width, self.__height
    
    def getSquare(self):
        return self.__height*self.__width

    def getPerim(self):
        return (self.__width+self.__height)*2
    
    def getDiagon(self):
        return (self.__height**2 + self.__width**2)**(-2)

    def printFigure(self):
        for i in range(0, self.__height):
            print("*"*self.__width)

p1 = Rectangle(10, 12)
p1.setValue(5, 2)
print(p1.getValue())
print(p1.getSquare())
print(p1.getPerim())
print(p1.getDiagon())
p1.printFigure()