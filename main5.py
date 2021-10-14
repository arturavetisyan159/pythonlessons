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
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         self.value = value
#         print(f"Счет #{self.num}, принадлежащий {self.surname}, был октрыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num}, принадлежащий {self.surname}, был закрты")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Процент: {self.percent : .0%}")
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.value = self.value - val
#             print(f"{val} {Account.suffix} были успешно сняты.")
#             self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} быди успешно добавлены.")
#         self.print_balance()
#
#
# acc = Account("Долгих", 12321, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(3)
# Account.set_eur_rate(4)
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Саяхов")
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(300)
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)

class Time:
    timezone = 0

    def __init__(self, moment):
        if Time.check_time(moment):
            hour = int(moment.split(':')[0])
            minute = int(moment.split(':')[1])
            second = int(moment.split(':')[2])
            self.hour = hour
            self.minute = minute
            self.second = second
            if Time.timezone >= 0:
                print(f"Отметка времени: {self.hour}:{self.minute}:{self.second} UTC+{Time.timezone}")
                print("--------------------")
            else:
                print(f"Отметка времени: {self.hour}:{self.minute}:{self.second} UTC{Time.timezone}")
                print("--------------------")
        else:
            print("Неверные данные.")
            print("--------------------")

    @classmethod
    def timezone_change(cls, zone):
        if isinstance(zone, int) and zone >= -12 and zone <= 14:
            cls.timezone = zone
            if cls.timezone >= 0:
                print(f"UTC+{cls.timezone}")
            else:
                print(f"UTC{cls.timezone}")
        else:
            print("Неверно введен часовой пояс!")

    @staticmethod
    def check_time(moment):
        if moment.count(":") != 2:
            return False
        else:
            moment = moment.split(':')
            hr = int(moment[0])
            min = int(moment[1])
            sec = int(moment[2])
            if hr > 24 or hr < 0 or min > 59 or min < 0 or sec > 59 or sec < 0:
                return False
            return True

    @staticmethod
    def sec_to_moment(second):
        second

    @staticmethod
    def moment_to_sec(moment):
        if 









t1 = Time("21:31:11")
Time.timezone_change(-2)





























