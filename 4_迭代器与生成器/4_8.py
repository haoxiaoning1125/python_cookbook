# coding:utf-8

"""
跳过可迭代对象的开始部分
"""

from itertools import dropwhile


if __name__ == '__main__':
    with open('4_8.txt') as f:
        for line in dropwhile(lambda l: l.startswith('#'), f):
            print line,
