
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

            if t0 is None:
                t0 = t1

            if t1 - t0 > tm:
                cache.clear()
                t0 = t1

            key = args_to_key(args, kwargs)
            if key in cache:
                return cache[key]
            else:
                cache[key] = func(*args, **kwargs)
                return cache[key]

        return inner

    return decorator




@make_cache_time(80)
def slow_func(*args, **kwargs):
    time.sleep(2)
    return args, len(kwargs)

@make_cache_time(8)
def slow_func_2(*args, **kwargs):
    time.sleep(2)
    return args, len(kwargs)



