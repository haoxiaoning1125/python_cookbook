# coding:utf-8

"""
多行匹配模式
"""

import re


if __name__ == '__main__':
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    ... multiline comment */
    ... '''
    print comment.findall(text1)
    print comment.findall(text2)
    print '-' * 20

    #
    comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
    print comment2.findall(text2)
