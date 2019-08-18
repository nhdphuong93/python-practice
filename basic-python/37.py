"""
37. Question:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10
"""

max_lim = int(raw_input())

even_numbers = [number for number in range(0, max_lim + 1) if number % 2 == 0]

print ",".join(map(str, even_numbers))
