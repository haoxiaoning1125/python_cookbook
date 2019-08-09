# coding:utf-8

"""
使用生成器创建新的迭代模式
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    # print [n for n in frange(15, 20, 0.5)]
    print list(frange(15, 20, 0.5))
