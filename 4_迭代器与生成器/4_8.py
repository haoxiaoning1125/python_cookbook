# coding:utf-8

"""
跳过可迭代对象的开始部分
"""

from itertools import dropwhile, islice


if __name__ == '__main__':
    # 根据某个测试函数跳过开始的元素
    with open('4_8.txt') as f:
        for line in dropwhile(lambda l: l.startswith('#'), f):
            print line,
    print '\n' + '-' * 20

    # 明确知道要跳过元素的个数
    items = ['a', 'b', 'c', 1, 4, 10, 15]
    print [x for x in islice(items, 3)]
    print [x for x in islice(items, 3, None)]
