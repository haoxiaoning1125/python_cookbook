# coding:utf-8

"""
数字的四舍五入
"""

if __name__ == '__main__':
    # round()
    print round(1.23, 1)
    print round(1.27, 1)
    print round(-1.27, 1)
    print round(1.25361, 1)
    print round(1627731, -1)
    print round(1627731, -2)
    print '-' * 20

    # format()
    x = 1.23456
    print format(x, '0.2f')
    print format(x, '0.3f')
    print 'value is {:0.4f}'.format(x)

