# coding:utf-8

"""
反向迭代
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    # reversed()
    a = [1, 2, 3, 4]
    print [n for n in reversed(a)]

    # __reversed__() in Class
    cd = Countdown(10)
    print [x for x in cd]
    print [x for x in reversed(cd)]