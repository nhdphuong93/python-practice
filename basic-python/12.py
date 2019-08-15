"""
12. Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def is_even(num):
    return num % 2 == 0


def is_all_even_digits(num):
    while num / 10 != 0:
        if is_even(num % 10):
            return False
        num = num / 10
    return True


begin = 1000
end = 3000
result = []

for number in range(begin, end + 1):
    if is_all_even_digits(number):
        result.append(number)

print ",".join(map(str, result))
