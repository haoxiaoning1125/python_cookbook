# coding:utf-8

"""
大型数组运算
"""

import numpy as np


if __name__ == '__main__':
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print ax * 2
    print ax + 10
    print ax + ay
    print ax * ay
    print '-' * 20

    def f(x):
        return 3 * x ** 2 - 2 * x +7
    print f(ax)
    print np.sqrt(ax)
    print np.cos(ax)
    print '-' * 20

    # grid = np.zeros(shape=(10000, 10000), dtype=float)
    # grid += 10
    # print grid
    # print np.sin(grid)
    # print '-' * 20

    # Numpy 扩展了 Python 列表的索引功能
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print a
    print a[1]
    print a[:, 1]
    print a[1:3, 1:3]
    a[1:3, 1:3] += 10
    print a
