# coding:utf-8

"""
展开嵌套的序列
"""

from collections import Iterable


def flatten(items, ignore_trpes=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_trpes):
            pass
            # yield from flatten(x)
        else:
            yield x

if __name__ == '__main__':
    pass