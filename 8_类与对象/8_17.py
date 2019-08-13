# coding:utf-8

"""
创建不调用 __init__() 方法的实例
"""


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)


if __name__ == '__main__':
    d = Date.__new__(Date)
    data = {'year': 2012, 'month': 8, 'day': 29}
    for k, v in data.items():
        setattr(d, k, v)
    print d
