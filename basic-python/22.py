"""
22. Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key
alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
input_string = raw_input()

list_string = input_string.split()

list_unique_words = set(list_string)

result = []

for word in list_unique_words:
    result.append((word, list_string.count(word)))

result.sort()

for count in result:
    print ":".join(map(str, count))
