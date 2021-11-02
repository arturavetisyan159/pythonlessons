# Классы shape, triangle и тд
from abc import ABC, abstractmethod
import math

class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perim(self):
        raise ConnectionError(f"Дочерний класс должен содержать этот метод")

    @abstractmethod
    def square(self):
        raise ConnectionError(f"Дочерний класс должен содержать этот метод")
    
    @abstractmethod
    def draw(self):
        raise ConnectionError(f"Дочерний класс должен содержать этот метод")

    @abstractmethod
    def info(self):
        raise ConnectionError(f"Дочерний класс должен содержать этот метод")


class Square(Shape):
    def __init__(self, a, color="black"):
        super().__init__(color)
        self.__a = a

    def perim(self):
        return self.__a * 4

    def square(self):
        return self.__a ** 2

    def draw(self):
        for i in range(0, self.__a):
            for j in range(0, self.__a):
                print("*", end=" ")
                if j == self.__a - 1:
                    print("\n", end="")

    def info(self):
        print(f"Сторона : {self.__a}")
        print(f"Периметр: {self.perim()}")
        print(f"Площадь: {self.square()}")
        print(f"Цвет: {self.color}")
        print()
        self.draw()


class Rectangle(Shape):
    def __init__(self, a, b, color="black"):
        super().__init__(color)
        self.__a = a
        self.__b = b

    def perim(self):
        return self.__a * 2 + self.__b * 2

    def square(self):
        return self.__a * self.__b

    def draw(self):
        for i in range(0, self.__a):
            for j in range(0, self.__b):
                print("*", end=" ")
                if j == self.__b - 1:
                    print("\n", end="")

    def info(self):
        print(f"Сторона 1: {self.__a}")
        print(f"Сторона 2: {self.__b}")
        print(f"Периметр равен: {self.perim()}")
        print(f"Площадь равна: {self.square()}")
        print(f"Цвет - {self.color}")
        print()
        self.draw()


class Triangle(Shape):
    def __init__(self, a, b, c, color="black"):
        super().__init__(color)
        self.__a = a
        self.__b = b
        self.__c = c

    def perim(self):
        return self.__a + self.__b + self.__c

    def square(self):
        if self.__a != self.__b:
            raise ValueError("a должно быть равно b")
        h = math.sqrt(self.__a**2 - (self.__c / 2)**2)
        return (self.__b * h) / 2

    def draw(self):
        print("НЕ МОГУ НАРИСОВАТЬ ТРЕГУОЛЬНИК, СЛОМАЛ ГОЛОВУ")
    
    def info(self):
        print(f"Сторона 1: {self.__a}")
        print(f"Сторона 2: {self.__b}")
        print(f"Сторона 3: {self.__c}")
        print(f"Периметр равен: {self.perim()}")
        print(f"Площадь равна: {self.square()}")
        print(f"Цвет - {self.color}")
        print()
        self.draw()

sq1 = Square(11, "green")
rect1 = Rectangle(4, 5, "yellow")
triang1 = Triangle(20, 20, 28, "green")

sq1.info()
print()
rect1.info()
print()
triang1.info()

    





