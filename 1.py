import math

figure = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
if figure == 1:
    a = int(input("Длина прямоугольника = "))
    b = int(input("Ширина прямоугольника = "))
    def square(dl, sh):
        res = dl * sh
        return res
    result = square(a, b)
    print("Площадь прямоугольника =", result)

elif figure == 2:
    a = int(input("Основание = "))
    h = int(input("Высота = "))
    def square(osn, vys):
        res = (osn / 2) * vys
        return res
    result = square(a, h)
    print("Площадь треугольника =", result)

elif figure == 3:
    r = int(input("Радиус круга = "))
    def square(radius):
        res = math.pi * ((radius)**2)
        return res
    result = round(square(r), 2)
    print("Площадь круга =", result)

else:
    print("!Неправильно выбрана цифра, попробуйте еще раз!")