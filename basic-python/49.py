"""
49. Question:
Write a Python program to convert unix timestamp string to readable date.
Sample Unix timestamp string : 1284105682
Expected Output : 2010-09-10 13:31:22
"""
import datetime

inputTimestamp = int(raw_input())

readableDate = datetime.datetime.fromtimestamp(inputTimestamp)

print readableDate
