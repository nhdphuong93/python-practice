"""
26. Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both
included).
"""


def generate_list(min_num, max_num):
    result = []
    for i in range(min_num, max_num + 1):
        result.append(i ** 2)
    return result


def print_list(min_num, max_num):
    print generate_list(min_num, max_num)


print_list(1, 20)
