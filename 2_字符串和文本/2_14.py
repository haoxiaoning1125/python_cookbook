# coding:utf-8

"""
合并拼接字符串
"""

import random


if __name__ == '__main__':
    # join()
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print ' '.join(parts)
    print '.'.join(parts)

    # +
    a = 'Is Chicago'
    b = 'Not Chicago?'
    print a + ' ' + b

    # ???
    s = 'a''b'
    print s
    print '-' * 20

    # 优化
    # s = ''  # 低效率
    # for p in parts:
    #     s += p

    data = ['ACME', 50, 91.1]
    print ','.join(str(s) for s in data)

    # # Version 1 (string concatenation), 两个小字符串更优
    # f.write(chunk1 + chunk2)
    # # Version 2 (separate I/O operations), 两个大字符串更优
    # f.write(chunk1)
    # f.write(chunk2)

    def random_str_out():
        list_ = ['a', 'b', 'c', 'd']
        while True:
            yield random.choice(list_)
    print ','.join(str(random_str_out().next()) for i in range(10))

    
