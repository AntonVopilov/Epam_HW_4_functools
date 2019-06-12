
import functools
import random
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


def make_cache_time(tm):
    def decorator(func):
        cache = {}

        @functools.wraps(func)
        def inner(*args, **kwargs):
            t1 = time.time()
            key = args_to_key(args, kwargs)

            if (key in cache) and t1 - cache[key][1] < tm:
                return cache[key][0]
            else:
                cache[key] = func(*args, **kwargs), t1
                return cache[key][0]

        return inner

    return decorator


@make_cache_time(0.5)
def a_1(b):
    return random.choice(range(20))


@make_cache_time(5)
def a_2(b):
    return random.choice(range(20))


for i in range(5):
    time.sleep(0.25)
    print('a_1(i), a_2(i) = ', a_1(i), a_2(i))

for i in range(5):
    print('a_1(i), a_2(i) = ',a_1(i), a_2(i))




