
import functools
from collections import OrderedDict
import time
from datetime import datetime, timedelta

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


def make_cache_time(tm):
    def decorator(func):
        cache = {}

        t0 = None

        @functools.wraps(func)
        def inner(*args, **kwargs):
            nonlocal t0

            t1 = time.time()

            if not t0:
                t0 = t1

            if t1 - t0 > tm:
                cache.clear()
                t0 = t1
                print('clear')

            print(t1-t0)
            key = args_to_key(args, kwargs)
            if key in cache:
                print('use cache', key)
                return cache[key]
            else:
                print('calc func', key)
                cache[key] = func(*args, **kwargs)
                return cache[key]

        return inner

    return decorator





@make_cache_time(80)
def slow_func(*args, **kwargs):
    time.sleep(2)
    return args, len(kwargs)

@make_cache_time(6)
def slow_func_2(*args, **kwargs):
    time.sleep(2)
    return args, len(kwargs)

print(slow_func(1,2,3))
print(slow_func(1,2,171))
print(slow_func_2(1,2,10))
print(slow_func_2(1,2,11))

print(slow_func(1,2,4))
print(slow_func(1,2,5))
print(slow_func(1,2,3))
print(slow_func(1,2,6))
print(slow_func(1,2,7))
print(slow_func(1,2,8))
print(slow_func(1,2,9))
print(slow_func_2(1,2,10))




