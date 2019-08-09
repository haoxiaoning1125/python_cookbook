# coding:utf-8

"""
字符串转换为日期
"""

from datetime import datetime


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


if __name__ == '__main__':
    # datetime.strptime()
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print diff
    print datetime.strftime(z, '%A %B %d, %Y')
    print '-' * 20

    # strptime 性能较差, 在代码中需要解析大量的日期并且已经知道了日期字符串的确切格式，可以自己实现一套解析方案来获取更好的性能
    print parse_ymd('2019-11-25')
