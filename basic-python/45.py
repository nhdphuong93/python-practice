"""
45. Question:
Write a decorator which wraps functions to log function arguments and the return value on each call. Provide support for
both positional and named arguments (your wrapper function should take both *argsand **kwargs and print them both):

@logged
... def func(*args):
...   return 3 + len(args)
func(4, 4, 4)
you called func(4, 4, 4)
it returned 6
6
"""
from functools import wraps


def logged(func):
    @wraps(func)
    def my_log(*args, **kwargs):
        print len(args)
        print len(kwargs)
        return func(*args, **kwargs)
    return my_log


@logged
def some_test_func(a, b, c):
    return a + b + c


print some_test_func(4, 4, 4)
