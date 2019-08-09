# coding:utf-8

"""
执行精确的浮点数运算
"""

from decimal import Decimal, localcontext


if __name__ == '__main__':
    print '4.2 + 2.1 == 6.3? : {}'.format(4.2 + 2.1 == 6.3)
    print '-' * 20

    # Decimal
    a = Decimal('4.2')
    b = Decimal('2.1')
    print a + b
    print a + b == Decimal(6.3)
    print '-' * 20

    #
    a = Decimal('1.3')
    b = Decimal('1.7')
    print a / b
    with localcontext() as ctx:
        ctx.prec = 3
        print  a / b
        ctx.prec = 50
        print a / b