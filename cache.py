
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
        make_cache_time.end = datetime.now() + timedelta(seconds=tm)
        @functools.wraps(func)
        def inner(*args, **kwargs):

            if datetime.now() > make_cache_time.end:
                cache.clear()

            key = args_to_key(args, kwargs)
            if key in cache:
                return cache[key]
            else:
                cache[key] = func(*args, **kwargs)
                return func(*args, **kwargs)
        return inner
    return decorator

@make_cache_time(10)
def slow_func(*args, **kwargs):
    time.sleep(1)
    return args, len(kwargs)

@make_cache_time(10)
def slow_func_2(*args, **kwargs):
    time.sleep(1)
    return args, len(kwargs)


