"""
33. Question:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as
argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""


class Shape(object):

    def compute_area(self):
        return 0


class Square(Shape):
    length = 0

    def __init__(self, length):
        self.length = length

    def compute_area(self):
        return self.length ** 2


my_shape = Shape()
print my_shape.compute_area()

my_square = Square(100)
print my_square.compute_area()
