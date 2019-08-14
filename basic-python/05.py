"""
5. Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""


class IOString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = raw_input("Input a string: ")

    def print_string(self):
        print "UPPER CASE string: ", self.string.upper()


simple_io_string = IOString()

simple_io_string.get_string()

simple_io_string.print_string()
