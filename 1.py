# Функция, которая ищет расстояние между точками
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
y1 = int(input("y1 = "))
y2 = int(input("y2 = "))

def distance(xx1, yy1, xx2, yy2):
    dist = ((xx2 - xx1)**2 + (yy2 - yy1)**2)**(1/2)
    return dist

res = distance(x1,y1, x2, y2)

print("result =", res)
