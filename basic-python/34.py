"""
34. Question:
Define a custom exception class which takes a string message as attribute.
"""

class MyException:
    attribute = ""

    def __init__(self, attribute):
        self.attribute = attribute

    def print_stack_trace(self):
        print self.attribute


exception = MyException("Something went wrong!")
exception.print_stack_trace()
