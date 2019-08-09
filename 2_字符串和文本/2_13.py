# coding:utf-8

"""
字符串对齐
"""

if __name__ == '__main__':
    text = 'Hello World'

    # ljust(), rjust(), center()
    print text.ljust(20)
    print text.rjust(20)
    print text.center(20)
    print text.ljust(20, '*')
    print text.center(20, '-')
    print '-' * 20

    # format()
    print format(text, '>20')
    print format(text, '<20')
    print format(text, '^20')
    print format(text, '=>20s')
    print format(text, '*^20s')
    print format(text, '#<20s')
    print '{:>10s} {:>10s}'.format('Hello', 'world')
