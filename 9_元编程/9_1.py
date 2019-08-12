# coding:utf-8

"""
在函数上添加装饰器
一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数
"""

import time
from functools import wraps


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
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(100000)
    countdown(10000000)