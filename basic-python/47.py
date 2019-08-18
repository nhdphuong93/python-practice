"""
47. Question:
Write a Python program to find the length of the last word.
Input: Python Exercises
Output: 9
"""

input_string = raw_input()

input_words = input_string.split()

last_word = input_words[len(input_words) - 1]

print len(last_word)
