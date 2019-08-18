"""
50. Question:
Write a Python program to add 5 seconds with the current time.
Sample Data :
13:28:32.953088
13:28:37.953088
"""
import datetime

currentTime = datetime.datetime.now()

currentTimeAdditionalFiveSecond = currentTime + datetime.timedelta(0, 5)

print currentTime.time()
print currentTimeAdditionalFiveSecond.time()

