# coding:utf-8

"""
字符串搜索和替换
"""

import re
from calendar import month_abbr


if __name__ == '__main__':
    text = 'yeah, but no, but yeah, but no, but yeah'
    print text.replace('yeah', 'yep')
    print '-' * 20

    # re.sub()
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print '-' * 20

    # 相同模式多次替换, 先编译
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print datepat.sub(r'\3-\1-\2', text)
    print '-' * 20

    # 传递回调函数代替更复杂的替换
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    print datepat.sub(change_date, text)
    print '-' * 20

    # 统计替换次数
    print datepat.subn(r'\3-\1-\2', text)
