"""
20. Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""


class GeneratorDivisible:
    number = 0
    max_number = 0

    def __init__(self, limit):
        self.max_number = limit

    def is_divisible(self, to_check):
        return to_check % 7 == 0

    def generate_number(self):
        while self.number <= self.max_number:
            if self.is_divisible(self.number):
                yield self.number
            self.number = self.number + 1


result = [divisble_number for divisble_number in GeneratorDivisible(100000).generate_number()]

print ",".join(map(str, result))
