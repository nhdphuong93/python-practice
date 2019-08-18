"""
32. Question: Define a class named Circle which can be constructed by a radius. The Circle class has a method
which can compute the area.
"""
import math


class Circle:
    circle_radius = 0

    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def compute_area(self):
        return self.circle_radius ** 2 * math.pi


my_round = Circle(100)

print my_round.compute_area()
