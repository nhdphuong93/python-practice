"""
25. Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. The function should just print the values only.
"""


def generate_dictionary():
    num_dict = dict()
    for i in range(1, 21):
        num_dict[str(i)] = i ** 2
    return num_dict


def print_dictionary_value(in_dict):
    for item in in_dict.values():
        print item,


result = generate_dictionary()

print_dictionary_value(result)
