"""
13. Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3
"""

inputData = raw_input()

totalLetters = sum(char.isalpha() for char in inputData)

totalDigits = sum(char.isdigit() for char in inputData)

print "LETTERS ", totalLetters

print "DIGITS", totalDigits
