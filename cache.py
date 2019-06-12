
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

        @functools.wraps(func)
        def inner(*args, **kwargs):

            t1 = time.time()

            key = args_to_key(args, kwargs)
            if key in cache:
                print('use cache', key)
                t0 = cache[key][1]
                if t1 - t0 > tm:
                    print('rewrite', func.__name__, cache)
                    print(t1-t0)
                    cache[key] = func(*args, **kwargs), t1
                    print('after rewrite', func.__name__, cache)
                    return cache[key]
                else:
                    return cache[key]
            else:
                cache[key] = func(*args, **kwargs), t1
                print('calc func', func.__name__, cache)
                return cache[key][0]

        return inner

    return decorator




import random
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




