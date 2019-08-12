# coding:utf-8

"""
解除一个装饰器
"""

from functools import wraps
import time


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (func.__name__, end - start)
        return result
    return wrapper


@timethis
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(1, 1)
