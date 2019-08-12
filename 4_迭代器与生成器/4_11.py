# coding:utf-8

"""
同时迭代多个序列
"""

from itertools import izip_longest


if __name__ == '__main__':
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    print [(x, y) for x, y in zip(xpts, ypts)]

    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    print [(num_a, num_b) for num_a, num_b in zip(a, b)]

    print [(num_a, num_b) for num_a, num_b in izip_longest(a, b)]
    print [(num_a, num_b) for num_a, num_b in izip_longest(a, b, fillvalue=0)]
