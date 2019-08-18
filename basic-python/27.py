"""
27. Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last
half values in one line.
Hints: Use [n1:n2] notation to get a slice from a tuple.
"""

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
input_size = len(input_tuple)
input_half_size = int(round(input_size / 2))

print input_tuple[0: input_half_size]
print input_tuple[input_half_size: input_size]