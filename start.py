from geometry import rect
from geometry.sq import Square
from geometry.trian import Triangle

r1 = rect.Rectangle(10, 20)
r2 = rect.Rectangle(30, 40)


s1 = Square(10)
s2 = Square(20)

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.get_perim())
