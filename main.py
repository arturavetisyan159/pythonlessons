# Классы shape, triangle и тд
from abc import ABC, abstractmethod

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
    def __init__(self, a, color):
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
    def __init__(self, a, b, color):
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

sq1 = Square(11, "green")
rect1 = Rectangle(4, 5, "yellow")

sq1.info()
rect1.info()

    





