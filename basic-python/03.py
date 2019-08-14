"""3. Question: With a given integral number n, write a program to generate a dictionary that contains (i,
i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Suppose the following input is supplied to the program: 8

Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
Consider use dict()
"""


def generate_dict(number):
    result_dict = {}
    for number in range(1, number + 1):
        result_dict[number] = number * number
    return result_dict


input_number = int(raw_input("Given an integral number: "))

print generate_dict(input_number)
