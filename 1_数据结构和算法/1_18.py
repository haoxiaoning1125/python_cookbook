# coding:utf-8

"""
映射名称到序列元素
命名元组
"""

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


if __name__ == '__main__':
    ss = [[1, 2, 3], [2, 3, 4]]
    print compute_cost(ss)
