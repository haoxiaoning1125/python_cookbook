# coding:utf-8

"""
定义有默认参数的函数
"""

x = 42


def spam(a, b=21):
    print (a, b)


def spam2(a, b=x):
    print (a, b)


if __name__ == '__main__':
    spam(1, 2)
    spam(1)
    print '-' * 20

    spam2(1, 2)
    spam2(1)
