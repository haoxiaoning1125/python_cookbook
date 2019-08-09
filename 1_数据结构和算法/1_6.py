# coding:utf-8

"""
multidict
一个键对应多个值
"""

from collections import defaultdict

if __name__ == '__main__':
    d1 = defaultdict(list)
    d1['a'].append(1)
    d1['a'].append(2)
    d1['a'].append(2)
    d1['b'].append(4)
    print d1
    print '-' * 20

    d2 = defaultdict(set)
    d2['a'].add(1)
    d2['a'].add(2)
    d2['a'].add(2)
    d2['b'].add(4)
    print d2
    print '-' * 20

    d3 = {}
    d3.setdefault('a', []).append(1)
    d3.setdefault('a', []).append(2)
    d3.setdefault('b', []).append(4)
    # print d3.setdefault('c', [])
    print d3
    print '-' * 20

    pairs = [['a', 1], ['a', 2], ['a', 3], ['b', 1], ['b', 2]]

    d4 = {}
    for k, v in pairs:
        if k not in d4:
            d4[k] = []
        d4[k].append(v)
    d5 = defaultdict(list)
    for k, v in pairs:
        d5[k].append(v)
    print d4
    print d5
