# coding:utf-8

"""
在类中定义多个构造器
使用 __init__() 之外的方法初始化
"""

import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class NewDate(Date):
    pass


if __name__ == '__main__':
    a = Date(2019, 8, 12)
    print a
    b = Date.today()
    print b
    c = NewDate.today()
    print c
