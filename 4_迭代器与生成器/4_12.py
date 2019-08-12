# coding:utf-8

"""
不同集合上元素的迭代
"""

from itertools import chain


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = ['a', 'b', 'c']
    print [x for x in chain(a, b)]
    print '-' * 20

    active_items = set()
    inactive_items = set()
    print [x for x in chain(active_items, inactive_items)]

    
