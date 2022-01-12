from functools import lru_cache

sum = 11


@lru_cache()
def calc(days, sum):
    if days < 1:
        return 11

    return calc(days-1) * 3


print(calc(20))
