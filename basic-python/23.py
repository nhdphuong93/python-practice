"""
23. Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator
"""


def calculate_square(to_calc):
    return to_calc ** 2


input_data = int(raw_input())

print calculate_square(input_data)
