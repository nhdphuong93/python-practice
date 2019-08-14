"""
4. Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number.

Suppose the following input is supplied to the program:
34,67,55,33,12,98

Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
"""


def convert_to_string(string):
    return list(string.split(","))


def convert_to_tuple(string):
    return tuple(string.split(","))


input_string = raw_input("Given a sequence comma-separated numbers: ")

print convert_to_string(input_string)

print convert_to_tuple(input_string)
