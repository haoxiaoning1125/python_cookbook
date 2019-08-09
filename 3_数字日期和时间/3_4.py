# coding:utf-8

"""
2, 8, 16 进制整数
"""

if __name__ == '__main__':
    x = 1234
    print bin(x)  # 2
    print oct(x)  # 8
    print hex(x)  # 16
    print '-' * 20

    print format(x, 'b')  # 2
    print format(x, 'o')  # 8
    print format(x, 'x')  # 16
    print '-' * 20

    print int('4d2', 16)
    print int('10011010010', 2)
