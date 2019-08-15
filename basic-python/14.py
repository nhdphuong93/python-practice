"""
14. Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

inputData = raw_input()

totalUpperCase = sum(char.isupper() for char in inputData)

totalLowerCase = sum(char.islower() for char in inputData)

print "UPPER CASE", totalUpperCase

print "LOWER CASE", totalLowerCase
