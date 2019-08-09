# coding:utf-8

"""
排列组合的迭代
"""

from itertools import (
    permutations, combinations, combinations_with_replacement
)


if __name__ == '__main__':
    items = ['a', 'b', 'c']

    # itertools.permutations(), 排列
    print [p for p in permutations(items)]

    # 指定长度的所有排列
    print [p for p in permutations(items, 2)]
    print '-' * 20

    # itertools.combinations(), 组合
    print [c for c in combinations(items, 2)]

    # itertools.combinations_with_replacement(), 允许一个元素被使用多次
    print [cwr for cwr in combinations_with_replacement(items, 3)]