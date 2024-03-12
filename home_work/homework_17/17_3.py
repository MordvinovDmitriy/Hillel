#!/usr/bin/python3

class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x} y:{self.y}'


class circle(point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'x:{self.x} y:{self.y} radius:{self.radius}'

    def __sub__(self, other):
        new_circle_x = self.x - other.x
        new_circle_y = self.y - other.y
        if self.radius != other.radius:
            new_circle_radius = abs(self.radius - other.radius)
            return circle(new_circle_x, new_circle_y, new_circle_radius)
        else:
            return point(new_circle_x, new_circle_y)


'''
circle_1 = circle(3, 4, 5)
circle_2 = circle(6, 5, 6)
circle_sub = circle_1 - circle_2
print(circle_sub)
print(type(circle_sub))
print('-'*50)
circle_1 = circle(3, 4, 5)
circle_2 = circle(6, 5, 5)
circle_sub = circle_1 - circle_2
print(circle_sub)
print(type(circle_sub))
'''