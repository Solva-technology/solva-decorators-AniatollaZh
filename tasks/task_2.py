from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print("Из кэша")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
