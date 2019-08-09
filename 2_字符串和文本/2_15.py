# coding:utf-8

"""
字符串中插入变量
"""

if __name__ == '__main__':
    s = '{name} has {n} messages.'
    print s.format(name='S', n=37)

    # format 无法处理变量缺失
    try:
        print s.format(name='S')
    except Exception as e:
        print e
    print '-' * 20
