"""
38. Question:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"""

input_list = [2, 4, 6, 8]

for item in input_list:
    assert item % 2 == 0, "Found odd number!"

print input_list
