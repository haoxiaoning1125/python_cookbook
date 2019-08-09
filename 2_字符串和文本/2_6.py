# coding:utf-8

"""
字符串忽略大小写的搜索替换
"""

import re


if __name__ == '__main__':
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print re.findall('python', text, flags=re.IGNORECASE)
    print re.sub('python', 'snake', text, flags=re.IGNORECASE)
    print '-' * 20

    # 辅助函数
    def matchcase(word):
        def replace(m):
            t = m.group()
            if t.isupper():
                return word.upper()
            elif t.islower():
                return word.lower()
            elif t[0].isupper():
                return word.capitalize()
            else:
                return word
        return replace
    print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
    print '-' * 20
