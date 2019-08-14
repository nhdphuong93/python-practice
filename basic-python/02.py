"""
2. Question:
Write a program which can compute the factorial of a given numbers.

Suppose the following input is supplied to the program:
8

Then, the output should be:
40320
"""


def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    else:
        return number


input_number = int(raw_input("Given a number: "))

print factorial(input_number)
