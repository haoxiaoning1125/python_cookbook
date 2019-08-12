# coding:utf-8

"""
减少可调用对象的参数个数
"""

from functools import partial


def spam(a, b, c, d):
    return a, b, c, d


if __name__ == '__main__':
    s1 = partial(spam, 1)
    print s1(2, 3, 4)
    print s1(4, 5, 6)
    print '-' * 20

    s2 = partial(spam, d=100)
    print s2(1, 2, 3)
    print s2(4, 5, 6)
    print '-' * 20

    s3 = partial(spam, 1, 2, d=200)
    print s3(2)
    print s3(1)