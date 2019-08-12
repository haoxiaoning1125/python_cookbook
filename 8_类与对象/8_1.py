# coding:utf-8

"""
改变对象的字符串显示
"""


# 优先级: __str()__ > __repr()__
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == '__main__':
    pair = Pair(11, 25)
    print pair

    print 'p is {0!r}'.format(pair)
    print 'p is {0}'.format(pair)
