# coding:utf-8

"""
命名切片
"""

if __name__ == '__main__':
    record = '....................100 .......513.25 ..........'
    cost1 = int(record[20:23]) * float(record[31:37])
    print ('cost1', cost1)
    print '-' * 20

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost2 = int(record[SHARES]) * float(record[PRICE])
    print ('cost2', cost2)
    print '-' * 20

    print ('PRICE.start:', PRICE.start, 'PRICE.stop:', PRICE.stop, 'PRICE.step:', PRICE.step)
    print '-' * 20

    # ???????????????????
    s = 'HelloWorld'
    a = slice(5, 10, 2)
    print a.indices(len(s))
    for i in range(*a.indices(len(s))):
        print s[i]
