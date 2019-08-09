# coding:utf-8

"""
字符串开头或结尾匹配
"""

import re


if __name__ == '__main__':
    # startswith(), endswith()
    filename = 'spam.txt'
    print filename.startswith('.txt')
    print filename.endswith('.txt')
    url = 'http://www.python.org'
    print url.startswith('http://') and url.endswith('.org')
    print '-' * 20

    file_names = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    print [fname for fname in file_names if fname.endswith(('.c', '.h'))]
    print '-' * 20

    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    try:
        print 'matched with []:{}'.format(url.startswith(choices))
    except:
        print 'matched with (): {}'.format(url.startswith(tuple(choices)))
    print '-' * 20

    # 使用切片代替
    filename = 'spam.txt'
    print filename[-4:] == '.txt'
    url = 'http://www.python.org'
    print url[:5] == 'http:' or url[:6] == 'https' or url[:4] == 'ftp:'

    # 使用正则代替
    url = 'http://www.python.org'
    print re.match('http:|https:|ftp::', url)
