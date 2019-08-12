# coding:utf-8

"""
内联回调函数
"""


def apply_async(func, callback, *args):
    result = func(*args)
    callback(result)


if __name__ == '__main__':
    pass
