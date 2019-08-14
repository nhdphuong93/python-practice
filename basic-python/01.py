"""
1. Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
and 3200 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""

begin = 2000
end = 3200
result = []

for number in range(begin, end + 1):
    divisionCondition = number % 7 == 0
    multipleCondition = number % 5 != 0
    if divisionCondition and multipleCondition:
        result.append(number)

print ', '.join(map(str, result))
