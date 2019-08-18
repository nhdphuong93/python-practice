"""
40. Question:
Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list.

Hints:
Use if/elif to deal with conditions.
"""
import random


def binary_search(sorted_list, left, right, item):
    while left <= right:
        mid = left + right / 2

        if sorted_list[mid] == item:
            return mid

        elif sorted_list[mid] > item:
            right = mid - 1

        else:
            left = mid + 1
    return -1


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print binary_search(input_list, 0, len(input_list) - 1, 15)
print binary_search(input_list, 0, len(input_list) - 1, 5)
