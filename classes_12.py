import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, coordinates: Point, r):
        self.coordinates = coordinates
        self.r = r

    def perimeter(self):
        return round(self.r * (2 * 3.14), 2)

    def area(self):
        return round(3.14 * self.r ** 2, 2)


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        side_ab = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        print(side_ab)
        side_bc = math.sqrt((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2)
        print(side_bc)
        side_ca = math.sqrt((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2)
        print(side_ca)
        return round(side_ab + side_bc + side_ca, 2)

    def area(self):
        side_ab = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        side_bc = math.sqrt((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2)
        side_ca = math.sqrt((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2)
        p = (side_ab + side_bc + side_ca) / 2
        return round(math.sqrt(p * (p - side_ab) * (p - side_bc) * (p - side_ca)), 2)


class Square:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def perimeter(self):
        side = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        return round(side * 4, 2)

    def area(self):
        side = math.sqrt((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2)
        return round(side * 2, 2)
