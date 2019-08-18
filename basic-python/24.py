"""
24. Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""


class SimpleClass:
    class_number = 1

    def __init__(self, input_num):
        self.class_number = input_num

    def print_class_number(self):
        print self.class_number


test_class = SimpleClass(100)

test_class.print_class_number()
