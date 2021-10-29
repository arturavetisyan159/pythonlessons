# Перегруз методов 

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if (x > 9) else "0" + str(x)

    def get_second(self):
        return self.__sec

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.__sec - other.get_second())

    def __floordiv__(self, other):
        res = self.__sec // other.get_second()
        return Clock(res)

    def __mul__(self, other):
        res = self.__sec * other.get_second()
        return Clock(res)

    def __mod__(self, other):
        res = self.__sec % other.get_second()
        return Clock(res)

    def __isub__(self, other):
        self.__sec = self.__sec - other.get_second()
        return self.__sec



c1 = Clock(600)
c2 = Clock(260)
print(f"c1 = {c1.get_format_time()}")
print(f"c2 = {c2.get_format_time()}")
print()

res = c1 - c2
print(f"c1 - c2 = {res.get_format_time()}")
res = c1 // c2
print(f"c1 // c2 = {res.get_format_time()}")
res = c1 * c2
print(f"c1 * c2 = {res.get_format_time()}")
res = c1 % c2
print(f"c1 % c2 = {res.get_format_time()}")
c1 -= c2
print(f"c1 -= c2 : {res.get_format_time()}")
