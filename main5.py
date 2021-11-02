from abc import abstractmethod
from datetime import datetime
import math
from abc import abstractmethod, ABC


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
# class Rectangle:

#     def __init__(self, w=0, h=0):
#         self.__width = w
#         self.__height = h
    
#     def setValue(self, w, h):
#         self.__width = w
#         self.__height = h

#     def getValue(self):
#         return self.__width, self.__height
    
#     def getSquare(self):
#         return self.__height*self.__width

#     def getPerim(self):
#         return (self.__width+self.__height)*2
    
#     def getDiagon(self):
#         return (self.__height**2 + self.__width**2)**(-2)

#     def printFigure(self):
#         for i in range(0, self.__height):
#             print("*"*self.__width)

# p1 = Rectangle(10, 12)
# p1.setValue(5, 2)
# print(p1.getValue())
# print(p1.getSquare())
# print(p1.getPerim())
# print(p1.getDiagon())
# p1.printFigure()

##############################

# __getattr__(self, item) (вызывается, когда атрибут не существует)
# __getattribute__(self, item) (вызывается при вызове лбюого атрибута, неважно, сущ или не сущ)
# __setattr__(self, name, value) (вызывается при измененении атрибута)
# __slots__ ()

##############################

# class Point:

#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __checkValue(z):
#         if (isinstance(z, int) or isinstance(z, float)):
#             return True
#         return  False
    
#     # def setValue(self, x, y):
#     #     if Point.__checkValue(x) and Point.__checkValue(y):
#     #         self.__x = x
#     #         self.__y = y
#     #     else:
#     #         print("Координаты должны быть чсилами!")

#     def __setValue_x(self, x):
#         if Point.__checkValue(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")

#     def __getValue_x(self):
#         return self.__x

#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x

#     coordX = property(__getValue_x, __setValue_x, __del_coords_x)

# p1 = Point(5, 10)
# p1.coordX = 100
# x = p1.coordX
# print(x)
# del p1.coordX  

############################
# Исопользование декораторов в классах

# class Point:

#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __checkValue(z):
#         if (isinstance(z, int) or isinstance(z, float)):
#             return True
#         return  False

#     @property
#     def coords_x(self):
#         return self.__x

#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__checkValue(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")

#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x

#     # coordX = property(__getValue_x, __setValue_x, __del_coords_x)

# p1 = Point(5, 10)
# p1.coordX = 100
# x = p1.coordX
# print(x)
# del p1.coordX  

#######################
# Задача кг в фунты

# class Converter:

#     def __init__(self, kg=0, f=0):
#         self.__kg = kg
#         self.__f = f
    
#     def __check_value(item):
#         if isinstance(item, int) or isinstance(item, float):
#             return True
#         return False

#     @property
#     def kg_get(self):
#         return self.__kg

#     @kg_get.setter
#     def kg_get(self, kg):
#         if Converter.__check_value(kg):
#             self.__kg = kg
#         else:
#             print("Неправильный формат данных.")

#     def converter(self):
#         self.__f = self.__kg * 2.985
#         return self.__f

# p1 = Converter()
# p1.kg_get = 12
# kg = p1.kg_get

# print(kg, "kg", "=>", p1.converter(), "fnt")
# print(p1.kg_get)

########################### Объекты-свойства (property)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __checkValue(x):
#         if isinstance(x, int):
#             return True
#         return False

#     @property
#     def coordX(self):
#         return self.__x

#     @coordX.setter
#     def coordX(self, x):
#         if Point.__checkValue(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
    
#     @coordX.deleter
#     def coordX(self):
#         print("Удаление свойства")
#         del self.__x


##############################

# Методы бывают: статические, класса (принимают класс в качестве параметра), экземпляра класса.
# Для работы со статическими методами мы должны использовать декоратор @staticmethod

# class Point:
#     __count = 0

#     def __init__(self, x=0, y=0):
#         Point.__count += 1
#         self.__x = x
#         self.__y = y

#     @staticmethod
#     def get_count():
#         return Point.__count


# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p3.get_count())

############################

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1

#     @staticmethod
#     def dec(x):
#         return x - 1

# print(Change.inc(10), Change.dec(10))

############################

# cls
# @classmethod

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_str):
#         day, month, year = map(int, date_str.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
# # date = Date.from_string("23/10/2021")
# # print(date.string_to_db())
# # date2 = Date.from_string("11.10.2022")
# # print(date2.string_to_db())
#
# dates = [
#     "30.22.2021",
#     "30-12-2021",
#     "30.12.2002",
#     "30.12.2021"
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         a = date.string_to_db()
#         print(a)
#     else:
#         print("Неправильная дата или формат строки с датой!")

####################
# ЗАДАНИЕ.

# class Account:
#     rate_usd = 0.014
#     rate_eur = 0.012
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"

#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname
#         self.__num = num
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был октрыт")
#         print("*" * 50)

#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был закрты")

#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate

#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate

#     @staticmethod
#     def convert(value, rate):
#         return value * rate

#     @property
#     def num(self):
#         return self.__num
    
#     @num.setter
#     def num(self, n):
#         self.__num = n

#     @property
#     def surname(self):
#         return self.__surname
    
#     @surname.setter
#     def surname(self, s):
#         self.__surname = s

#     @property
#     def percent(self):
#         return self.percent

#     @percent.setter
#     def percent(self, p):
#         self.__percent = p

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, v):
#         self.__value = v

#     def print_balance(self):
#         print(f"Текущий баланс: {self.__value} {Account.suffix}")

#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Процент: {self.__percent : .0%}")
#         print("-" * 20)

#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")

#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()

#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.__value = self.__value - val
#             print(f"{val} {Account.suffix} были успешно сняты.")
#             self.print_balance()

#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} быди успешно добавлены.")
#         self.print_balance()


# acc = Account("Долгих", 12321, 0.03, 1000)
# acc.print_info()
# acc.num = 1984
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(3)
# Account.set_eur_rate(4)
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.surname = "Иванов"
# acc.percent = 0.15
# acc.value = 2000
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(300)
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)


########################
# Наследование.

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"{self.__x}, {self.__y}"

# class Prop:
#     def __init__(self, sp:Point, ep:Point, color:str = "blue", width:int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width

#     def get_width(self):
#         return self.__width

    

# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор класса Line")
#         super().__init__(*args)
#         self.__width = 5


#     def draw_line(self):
#         print(f"Рисование линии: ({self._sp}), ({self._ep}), {self._color}, {self.__width}")

        
# class Rect(Prop):
    
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: ({self._sp}), ({self._ep}), {self._color}, {self.__width}")


# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)
# line.draw_line()

# class Figure:
#     def __init__(self, color):
#         self.__color = color

#     @property
#     def color(self):
#         return self.__color

#     @color.setter
#     def color(self, c):
#         self.__color = c


# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError

#     def area(self):
#         return f"Площадь равна {self.__height * self.__width}"

# rect = Rectangle(10, 20, "green")
# print(rect.width)
# rect.width = 11
# print(rect.width)
# print(rect.area())

# class Liquid:
#     def __init__(self, name, density):
#         self.__name = name
#         self.__density = density
    
#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, n):
#         self.__name = n

#     @property
#     def density(self):
#         return self.__density 
    
#     @density.setter
#     def density(self, d):
#         if isinstance(d, int) or isinstance(d, float) and d >= 0:
#             self.__density = d


#     def change_density(self, dens):
#         if isinstance(dens, int) or isinstance(dens, float) and dens >= 0:
#             self.__density = dens
#         else:
#             print("Неправильно задано значение плотности.")

#     def liquid_info(self):
#         return f"{self.__name} с плотнотстью {self.__density} kg/m^3"
    
#     def count_volume(self, mass):
#         result = round(mass / self.__density, 2)
#         print(f"Объем {mass} kg жидкости \"{self.__name}\" равен {result} m^3")
#         return result

#     def count_mass(self, volume):
#         result = round(volume * self.__density)
#         print(f"Масса {volume} m^3 жидкости \"{self.__name}\" равна {result} kg")
#         return result



# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.__strength = strength

#     @property
#     def strength(self):
#         return self.__strength
    
#     @strength.setter
#     def strength(self, s):
#         self.__strength = s

#     def change_strength(self, s):
#         self.__strength = s

#     def liquid_info(self):
#         return super().liquid_info() + f" крепость равна {self.__strength} %"



# lqd1 = Liquid("Сок", 1500)
# print(lqd1.liquid_info())
# print(lqd1.name)
# lqd1.count_volume(500)
# lqd1.count_mass(0.5)

# alco = Alcohol("Водка", 1000, 40)
# print(alco.liquid_info())

############################

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"{self.__x}, {self.__y}"

#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False

#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False


# class Prop:
#     def __init__(self, sp:Point, ep:Point, color:str = "blue", width:int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#             print("Успешно измененно")
#         else:
#             print("Координаты должны быть числами!")
    
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: ({self._sp}), ({self._ep}), {self._color}, {self._width}")

#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#             print("Координаты были успешно изменены.")
#         else:
#             print("Координаты должны быть числами!")

# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: ({self._sp}), ({self._ep}), {self._color}, {self._width}")

# line = Line(Point(1, 2), Point(20, 30))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
# print()
# rect = Rect(Point(5, 7), Point(50, 70))
# rect.draw_rect()
# rect.set_coords(Point(10, 20), Point(100, 200))
# rect.draw_rect()

######################################

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина: {self.width} \nВысота: {self.height}")


# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background

#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.fon}")


# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border

#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.border}")


# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()

############################

# class Liquid:
#     def __init__(self, name, density):
#         self.__name = name
#         self.__density = density
    
#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, n):
#         self.__name = n

#     @property
#     def density(self):
#         return self.__density 
    
#     @density.setter
#     def density(self, d):
#         if isinstance(d, int) or isinstance(d, float) and d >= 0:
#             self.__density = d


#     def change_density(self, dens):
#         if isinstance(dens, int) or isinstance(dens, float) and dens >= 0:
#             self.__density = dens
#         else:
#             print("Неправильно задано значение плотности.")

#     def liquid_info(self):
#         return f"{self.name} (плотнотсть = {self.density} kg/m^3)"
    
#     def count_volume(self, mass):
#         result = round(mass / self.__density, 2)
#         print(f"Объем {mass} kg жидкости \"{self.__name}\" равен {result} m^3")
#         return result

#     def count_mass(self, volume):
#         result = round(volume * self.__density)
#         print(f"Масса {volume} m^3 жидкости \"{self.__name}\" равна {result} kg")
#         return result



# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.__strength = strength

#     @property
#     def strength(self):
#         return self.__strength
    
#     @strength.setter
#     def strength(self, s):
#         self.__strength = s

#     def change_strength(self, s):
#         self.__strength = s

#     def count_volume(self, mass):
#         res = super().count_volume(mass)
#         result = res * self.strength / 100
#         print(f"Объем алкоголя в {mass} кг {self.name} составляет {result} m^3")
#         return res, result

#     def count_mass(self, volume):
#         value = super().count_mass(volume)
#         result = value * self.strength
#         print(f"Вес алкоголя {volume} m^3 {self.name} составляет {result} кг.")
#         return value, result

#     def liquid_info(self):
#         return f"{self.name} (плотнотсть = {self.density} kg/m^3, крепость = {self.strength})"



# lqd1 = Liquid("Сок", 1500)
# print(lqd1.liquid_info())
# print(lqd1.name)
# lqd1.count_volume(500)
# lqd1.count_mass(0.5)

# alco = Alcohol("Водка", 1000, 40)
# alco.count_volume(600)
# print(alco.liquid_info())

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"{self.__x}, {self.__y}"

#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False

#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False


# class Prop:
#     def __init__(self, sp:Point, ep:Point, color:str = "blue", width:int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#             print("Успешно измененно")
#         else:
#             print("Координаты должны быть числами!")
    
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: ({self._sp}), ({self._ep}), {self._color}, {self._width}")

#     def __set_one_coords(self, sp):
#         if sp.is_int():
#                 self._sp = sp
#                 print("Координаты были успешно измененны.")
#         else:
#                 print("Координаты должны быть целочисленными!")

#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#                 print("Координаты были успешно изменены.")
#         else:
#                 print("Координаты должны быть числами!")


#     def set_coords(self, sp, ep=None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)

# line = Line(Point(1, 2), Point(20, 30))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-1, -2))
# line.draw_line()

#############################

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"{self.__x}, {self.__y}"

#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False

#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False


# class Prop:
#     def __init__(self, sp:Point, ep:Point, color:str = "blue", width:int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#             print("Успешно измененно")
#         else:
#             print("Координаты должны быть числами!")

#     def draw(self):
#         raise NotImplementedError("В дочернем классе не определен метод draw.")


# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


# class Ellips(Prop):
#     def draw(self):
#         print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellips(Point(-50, -50), Point(-100, -100)))

# for fig in figs:
#     fig.draw()

# class Table():
#     def __init__(self, width=None, height=None, radius=None):
#         if radius == None:
#             self.width = width
#             self.height = height
#         else:
#             self.radius = radius


# class RoundTable(Table):
#     def __init__(self, radius):
#         super().__init__(width=None, height=None, radius=radius)
    
#     def calc_area(self):
#         return round(3.14 * self.radius**2, 2)


# class SquareTable(Table):
#     def __init__(self, width, height):
#         super().__init__(width=width, height=height, radius=None)

#     def calc_area(self):
#         return self.width * self.height

# t1 = SquareTable(10, 20)
# print(t1.__dict__)
# print(t1.calc_area())

# t2 = RoundTable(11)
# print(t2.__dict__)
# print(t2.calc_area())

######################################

# from abc import abstractmethod, ABC

# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску!")

#     @abstractmethod
#     def move(self):
#         pass

# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен на e2e4")


# q = Queen()
# q.draw()
# q.move()
    
######################################

# class Currency(ABC):
#     def __init__(self, value):
#         self.__value = value

#     @abstractmethod
#     def change_currency(self):
#         pass

#     def print_value(self):
#         print(self.__value, end=" ")

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, v):
#         self.__value = v

# class Dollar(Currency):
#     rate_usd = 74.16
#     suffix_usd = "USD"

#     def change_currency(self):
#         res = self.value * Dollar.rate_usd
#         return res

#     def print_value(self):
#         super().print_value()
#         print(f"{Dollar.suffix_usd} = {self.change_currency()} RUB")


# class Euro(Currency):
#     rate_eur = 90.14
#     suffix_eur = "EUR"

#     def change_currency(self):
#         res = self.value * Euro.rate_eur
#         return res

#     def print_value(self):
#         super().print_value()
#         print(f"{Euro.suffix_eur} = {self.change_currency()} RUB")




# n = [Euro(112), Euro(91), Euro(3311)]
# for elem in n:
#     elem.print_value()

# print()

# usd = [Dollar(121), Dollar(11), Dollar(10)]
# for elem in usd:
#     elem.print_value()

######################################

# class Creature:
#     def __init__(self, name):
#         self.name = name


# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")


# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")


# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")


# bob = Dog("Bob")
# bob.sleep()
# bob.play()
# bob.bark()

################################

# class A:
#     def __init__(self):
#         print("Инициализатор класса A")

# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")

#     def hi(self):
#         print("B")

# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")

#     def hi(self):
#         print("C")

# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор класса D")

#     def call_hi(self):
#         C.hi(self)

        
# d = D()
# d.call_hi()


################################

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
    
#     def __str__(self):
#         return f"{self.__x, self.__y}"


# class Styles:
#     def __init__(self):
#         print("Инициализатор Styles")
#         # super().__init__()


# class Pos:
#     def __init__(self):
#         print("Инициализатор Pos")
#         # super().__init__()


# class Line(Styles, Pos):
#     def __init__(self, sp=Point, ep=Point, color="green", width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#     def draw(self):
#         print(f"Рисуем линию: {self._sp}, {self._ep}, {self._color}, {self._width}")


# line1 = Line(Point(10,10), Point(12, 12), "green")
# line1.draw()


################################

# Mixins

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)

    
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)

#     def display(self, message):
#         super().display(message)
#         self.log(message)


# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message):
#         super().log(message, filename="subclasslog.txt")


# subclass = MySubClass()
# subclass.display("Эта строка будет отображаться и регистрироваться в файле subclasslog.txt")

################################

# Перегрузка операторов

# class Clock:
#     __DAY = 86400

#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.__sec = sec % self.__DAY

#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

#     @staticmethod
#     def __get_form(x):
#         return str(x) if (x > 9) else "0" + str(x)

#     def get_second(self):
#         return self.__sec

#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.__sec + other.get_second())

#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         self.__sec += other.get_second()
#         return self

#     def __eq__(self, other):
#         return self.__sec == other.get_second()

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __lt__(self, other):
#         return self.__sec < other.get_second()

#     def __le__(self, other):
#         return self.__sec <= other.get_second()

#     def __gt__(self, other):
#         return self.__sec > other.get_second()
    
#     def __ge__(self, other):
#         return self.__sec >= other.get_second()

#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
        
#         if item == "hour":
#             return (self.__sec // 3600) % 24
#         elif item == "minute":
#             return (self.__sec // 60) % 60
#         elif item == "second":
#             return self.__sec % 60

#         return "Неверный ключ"

#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
        
#         if not isinstance(value, int):
#             return ValueError("Значение должно быть числом")

#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24

#         if key == "hour":
#             self.__sec = s + 60 * m + value * 3600
#         elif key == "minute":
#             self.__sec = s + value * 60 + h * 3600
#         elif key == "second":
#             self.__sec = value + 60 * m + h * 3600



# c1 = Clock(101)
# c2 = Clock(100)
# print("c1 > с2", c1 > c2)
# print("c1 >= с2", c1 >= c2)
# print("c1 < c2", c1 < c2)
# print("c1 <= c2", c1 <= c2)

# print(c1["hour"], c1["minute"], c1["second"])
# c1["hour"] = 10
# print(c1.get_format_time())
# c1["minute"] = 10
# print(c1.get_format_time())
# c1["second"] = 10
# print(c1.get_format_time())

###############################
# ПОЛИМОРФИЗМ
###############################

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
    
#     def get_perim(self):
#         return (self.w + self.h) * 2
    

# class Square:
#     def __init__(self, a):
#         self.a = a
    
#     def get_perim(self):
#         return self.a * 4


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def get_perim(self):
#         return self.a + self.b + self.c

# r1 = Rectangle(10, 20)
# r2 = Rectangle(30, 40)

# # print(r1.get_perim_rect(), r2.get_perim_rect())
# # print()

# s1 = Square(10)
# s2 = Square(20)

# # print(s1.get_perim_sq(), s2.get_perim_sq())

# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)


# shape = [r1, r2, s1, s2, t1, t2]

# for g in shape:
#     print(g.get_perim())

#####################################

# class Cat:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def info(self):
#         print(f"Я кот. Меня зовут {self.__name}. Мне {self.__age}")

#     def make_sound(self):
#         print(f"{self.__name} мяукает")

# class Dog:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def info(self):
#         print(f"Я собака. Меня зовут {self.__name}. Мне {self.__age}")

#     def make_sound(self):
#         print(f"{self.__name} гавкает")

# animal1 = Cat("Тайсон", 2.3)
# animal2 = Dog("Ролик", 3)

# an_list = (animal1, animal2)
# for animal in an_list:
#     animal.info()
#     animal.make_sound()

##################################

# class Human:
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age

#     def info(self):
#         return f"{self.lastname} {self.name} {self.age} лет."


# class Student(Human):
#     def __init__(self, name, lastname, age, spec, group, rate):
#         super().__init__(name, lastname, age)
#         self.spec = spec
#         self.group = group
#         self.rate = rate
    
#     def info(self):
#         res = super().info()
#         return res + f" Специализация-{self.spec}, группа {self.group}, рейтинг {self.rate}."

# class Graduate(Student):
#     def __init__(self, name, lastname, age, spec, group, rate, diploma_theme):
#         super().__init__(name, lastname, age, spec, group, rate)
#         self.diploma_theme = diploma_theme
    
#     def info(self):
#         res = super.info()
#         return res + f" Тема дипломной работы - {self.diploma_theme}"

# class Teacher(Human):
#     def __init__(self, name, lastname, age, exp, spec):
#         super().__init__(name, lastname, age)
#         self.exp = exp
#         self.spec = spec

#     def info(self):
#         res = super().info()
#         return res + f"Специализация - {self.spec}, опыт работы - {self.exp}"


# group = [
#     Student("Артур", "Аветисян", 21, "Программирование", 1904, 1),
#     Graduate("Олег", "Тинькофф", 51, "Программирование", 1905, 2, "Внешшня безопасность"),
#     Teacher("Олег", "Великий учитель", 51, "800 лет", "компьютерная безопасность")
# ]

# print(group[0].info())
# # print(group[1].info())
# print(group[2].info())

##################################

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"{self.__class__} : {self.name}"

#     def __str__(self):
#         return f"{self.name}"

# cat = Cat("Пушок")
# print(cat)

##################################

# class Point:
#     def __init__(self, *args):
#         self.__cords = args
    
#     def __len__(self):
#         return len(self.__cords)

#     def __abs__(self):
#         return list(map(abs, self.__cords))


# p = Point(1, 2)
# print(len(p))
# print(abs(p))

##################################
# import math


# class Point:
#     __slots__ = ("x", "y", "__length")

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = round(math.sqrt(x*x + y*y), 1)

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, value):
#         self.__length = value

# class Point3D(Point):
#     __slots__ = ("z")

#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z




# pt = Point(1, 2)
# print(pt.length)
# pt.length = 10
# print(pt.length)
# pt3 = Point3D(10, 20, 30)
# print(pt3.x, pt3.y, pt3.z)

##################################
# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0

#     def __call__(self):
#         self.__counter += 1
#         print(f"counter = {self.__counter}")
#         return self.__counter


# c1 = Counter()
# c1()
# c1()

# c2 = Counter()
# c2()
# c2()
# c2()

##################################

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars

#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
        
#         return args[0].strip(self.__chars)

# s1 = StripChars("?:!., ")
# print(s1(" Hello, World! "))

# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string[0], str):
#             raise ValueError("Аргумент должен быть строкой")

#         return string.strip(chars)
#     return wrap

# s1 = strip_chars("?:!., ")
# print(s1(" Hello, World! "))

################################

# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     @property
#     def data(self):
#         return self.name, self.surname, self.age

#     def __str__(self):
#         return f"{self.name}, {self.surname}, {self.age}"


# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
    
#     def __call__(self, lst):
#         lst.sort(key= lambda i: [i.__dict__ for key in self.__method])





# p = [
#     Person("Artur", "Avetisyan", 20),
#     Person("Elena", "Vasilieva", 40),
#     Person("Pavel", "Sentyakov", 23),
#     Person("Alexander", "Sannikov", 21)
# ]

# print(p)

#######################################












    














