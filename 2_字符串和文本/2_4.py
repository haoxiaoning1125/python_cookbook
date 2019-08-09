# coding:utf-8

"""
字符串匹配和搜索
"""

import re


if __name__ == '__main__':
    text = 'yeah, but no, but yeah, but no, but yeah'
    print text == 'yeah'
    print text.startswith('yeah')
    print text.endswith('no')
    print text.find('no')
    print '-' * 20

    ts = ['11/27/2012', 'Nov 27, 2012']
    print [1 if re.match(r'\d+/\d+/\d+', t) else 0 for t in ts]
    print '-' * 20

    # 用同一个模式做多次匹配
    datepat = re.compile(r'\d+/\d+/\d+')
    print [1 if datepat.match(t) else 0 for t in ts]
    print '-' * 20

    # match() 从开始匹配, findall() 查找任意部分
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print datepat.findall(text)
    print '-' * 20

    # 捕获分组
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('11/27/2012')
    print [m.group(i) for i in range(4)]
    print m.groups()
    month, day, year = m.groups()
    print datepat.findall(text)
    print ['{}-{}-{}'.format(year, month, day) for month, day, year in datepat.findall(text)]
