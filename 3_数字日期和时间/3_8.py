# coding:utf-8

"""
分数运算
"""

from fractions import Fraction


if __name__ == '__main__':
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print a + b
    print a * b
    print '-' * 20

    c = a * b
    print (c.numerator, c.denominator)
    print '-' * 20

    print float(c)
    print Fraction(*3.75.as_integer_ratio())