"""
46. Question:
Write a decorator to cache function invocation results. Store pairs arg:result in a dictionary in an attribute of the
function object. The function being memoized is:
def fibonacci(n):
  assert n >= 0
  if n < 2:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
"""

