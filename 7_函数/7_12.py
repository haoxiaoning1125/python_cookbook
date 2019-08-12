# coding:utf-8

"""
访问闭包中定义的变量
"""


def sample():
    n = 0
    def func():
        print ('n={}'.format(n))

    def get_n():
        return n


if __name__ == '__main__':
    pass
