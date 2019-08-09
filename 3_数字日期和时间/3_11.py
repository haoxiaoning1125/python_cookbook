# coding:utf-8

"""
随机选择
"""

import random


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6]
    print [random.choice(values) for i in range(10)]

    print random.sample(values, 4)

    random.shuffle(values)
    print values

    print [random.randint(0, 10) for i in range(10)]

    print [random.random() for i in range(10)]

    print bin(random.getrandbits(200))

