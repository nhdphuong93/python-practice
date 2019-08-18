"""
48. Question:
Write a Python program to create a LIFO queue.
Expected Output:
3 2 1 0
"""
from urllib3.util import queue

my_queue = queue.LifoQueue()

for num in range(10):
    my_queue.put(num)

while not my_queue.empty():
    print my_queue.get(),
