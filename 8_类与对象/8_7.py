# coding:utf-8

"""
在子类中调用父类的某个已经被覆盖的方法
"""


class A(object):
    def __init__(self):
        self.x = 0

    def spam(self):
        print 'A.spam'


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.y = 1

    def spam(self):
        print 'B.spam'
        super(B, self).spam()


if __name__ == '__main__':
    b = B()
    print (b.x, b.y)

    b.spam()
