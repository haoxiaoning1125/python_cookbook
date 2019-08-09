# coding:utf-8

"""
删除字符串中不需要的字符
"""

import re


if __name__ == '__main__':
    # strip()
    s = ' hello world \n'
    print s.strip()
    print s.lstrip()
    print s.rstrip()
    t = '-----hello====='
    print t.lstrip('-')
    print t.strip('-=')
    s1 = ' hello                      world \n'
    print s1.strip()
    print '-' * 20

    # replace()
    print s1.replace(' ', '')
    print '-' * 20

    # re
    print re.sub(r'\s+', ' ', s1)
    print '-' * 20


