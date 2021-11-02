class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def get_perim(self):
        return (self.w + self.h) * 2
    

class Square:
    def __init__(self, a):
        self.a = a
    
    def get_perim(self):
        return self.a * 4


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perim(self):
        return self.a + self.b + self.c
        