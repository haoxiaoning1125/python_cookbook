# coding:utf-8

"""
最短匹配模式
"""

import re


if __name__ == '__main__':
    # * 操作符, 贪婪模式
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    text2 = 'Computer says "no." Phone says "yes."'
    print str_pat.findall(text1)
    print str_pat.findall(text2)
    print '-' * 20

    # ? 修饰符, 非贪婪模式
    new_str_pat = re.compile(r'\"(.*?)\"')
    print new_str_pat.findall(text2)
    print '-' * 20
