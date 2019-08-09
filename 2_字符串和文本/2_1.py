# coding:utf-8

"""
使用多个界定符分割字符串
"""

import re


if __name__ == '__main__':
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print re.split(r'[;,\s]\s*', line)
    fields = re.split(r'(;|,|\s)\s*', line)
    print fields
    print re.split(r'(?:,|;|\s)\s*', line)
    values = fields[::2]
    print values
    delimiters = fields[1::2] + ['']
    print delimiters
    print ''.join(v + d for v, d in zip(values, delimiters))
