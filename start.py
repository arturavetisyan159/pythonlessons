from shape.cylinder import Cylinder 
from shape.circle import Circle
from shape.rectangle import Rectangle

circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]
rects = [Rectangle(3, 7), Rectangle(2, 7), Rectangle(19, 12)]
cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]
circle_max_s = max(circles, key=lambda c: c.get_circle_square())
rect_min_p = min(rects, key=lambda r: r.get_rect_perimeter()) 
cylinders_v = list(map(lambda c: c.get_volume(), cylinders)) 
cylinders_v_avg = sum(cylinders_v) / len(cylinders_v) 
print('*'*50) 
print('Окружность с наибольшей площадью:', end=' ') 
circle_max_s.print_circle() 
print('Прямоугольник с наименьшим периметром:', end=' ') 
rect_min_p.print_rect() 
print(f'Средний объем всех цилиндров: {cylinders_v_avg:.2f}')