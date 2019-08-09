# coding:utf-8

"""
过滤序列元素
"""

import math
from itertools import compress


if __name__ == '__main__':
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]

    # 列表推导式
    print [n for n in mylist if n < 0]
    print '-' * 20

    # 生成器表达式
    pos = (n for n in mylist if n < 0)
    for i in pos:
        print i
    print '-' * 20

    # filter()
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    def is_int(val):
        try:
            _ = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))
    print ivals
    print '-' * 20

    # 在过滤时转换数据
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print [math.sqrt(n) for n in mylist if n > 0]
    print '-' * 20

    # 将不符合条件的值用新值代替
    print [n if n > 0 else 0 for n in mylist]
    print [n if n < 0 else 0 for n in mylist]
    print '-' * 20

    # itertools.compress()
    addresses = [
        '5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK',
        '5645 N RAVENSWOOD', '1060 W ADDISON', '4801 N BROADWAY', '1039 W GRANVILLE'
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print more5
    print list(compress(addresses, more5))
