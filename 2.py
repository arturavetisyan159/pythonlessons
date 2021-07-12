import math

a = int(input("Сторона 1 = "))
b = int(input("Сторона 2 = "))
angle = int(input("Угол между сторонами = "))

def square(x, y, z):
    def radian_convert(ang):
        ang = (ang * math.pi) / 180
        return ang
    res = ((a * b) / 2) * math.sin(radian_convert(z))
    return res

result = square(a, b, angle)

print("Результат =", result)
