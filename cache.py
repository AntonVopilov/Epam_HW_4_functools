
import functools
from collections import OrderedDict
import time


def args_to_key(args, kwargs):
    res = OrderedDict(sorted(kwargs.items()))
    key = tuple([(key, value) for key, value in res.items()])
    return key.__add__(args)


def make_cache(size=10):
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = args_to_key(args, kwargs)
            if key in cache:
                return cache[key]
            else:
                if len(cache) < size:
                    cache[key] = func(*args, **kwargs)
                    return func(*args, **kwargs)
                else:
                    cache.popitem()
                    cache[key] = func(*args, **kwargs)
                    return func(*args, **kwargs)
        return inner
    return decorator


@make_cache(size=30)
def slow_func(*args, **kwargs):
    time.sleep(1)
    return len(args), len(kwargs)

print(slow_func(1, 2, 3, a=4, b=5))
print(slow_func(1, 2, 4, a=4, b=5))
print(slow_func(1, 2, 3, a=4, b=5))
print(slow_func(1, 2, 3, c=4, b=5))
print(slow_func(1, 2, 3, c=4, b=5))
