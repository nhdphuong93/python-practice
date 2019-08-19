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
from functools import wraps


def cache(func):
    cache_dict = func.cache_dict = {}
    @wraps(func)
    def my_cache(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache_dict:
            print "Found cache"
            return cache_dict[key]
        else:
            print "Add cache"
            cache_dict[key] = func(*args, **kwargs)
            return cache_dict[key]
    return my_cache


@cache
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(5)
print fibonacci(5)
print fibonacci(3)

