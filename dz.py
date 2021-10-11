class Sphere:
    def __init__(self, x=0, y=0, z=0, r=0):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__r = r

    def __checkValue(num):
        if isinstance(num, int):
            return True
        return False
    
    def set_radius(self, r):
        self.__r = r
    
    def set_center(self, x, y, z):
        if Sphere.__checkValue(x) and Sphere.__checkValue(y) and Sphere.__checkValue(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print("Точки должны быть целыми натуральными числами!")

    def get_volume(self):
        return round((4/3)*3.14*5**3, 1)

    def get_square(self):
        return round(4*3.14*self.__r**2, 1)

    def get_radius(self):
        return self.__r

    def get_center(self):
        return self.__x, self.__y, self.__z

    def is_point_inside(self, x, y, z):
        if x <= self.__x and y <= self.__y and z <= self.__z:
            return True
        return False

sphere = Sphere()
sphere.set_center(1, 3, 3)
sphere.set_radius(5)
print(sphere.get_center())
print(sphere.get_radius())
print(sphere.is_point_inside(1, 1, 1))
print(sphere.get_square())
print(sphere.get_volume())
