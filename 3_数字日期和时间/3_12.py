# coding:utf-8

"""
基本的日期与时间转换
"""

from datetime import timedelta
from datetime import datetime


if __name__ == '__main__':
    # timedelta
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b

    print c.days
    print float(c.seconds) / 3600
    print c.total_seconds()
    print '-' * 20

    # datetime
    a = datetime(2012, 9, 23)
    print a + timedelta(days=10)
    b = datetime(2012, 12, 21)
    c = b - a
    print 'c.days: {}'.format(c.days)
    now = datetime.today()
    print now
    print now + timedelta(minutes=10)
    print '-' * 20

    # datetime 自动处理闰年
    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print 'a - b: {}, (a - b).days: {}'.format(a - b, (a - b).days)
    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    print 'c - d: {}, (c - d).days: {}'.format(c - d, (c - d).days)
