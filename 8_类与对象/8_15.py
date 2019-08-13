# coding:utf-8

"""
属性的代理访问
代理模式: 将某个操作转移给另外一个对象来实现
"""


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print ('getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Proxy, self).__setattr__(name, value)
        else:
            print ('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super(Proxy, self).__delattr__(name)
        else:
            print ('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print ('Spam.bar:', self.x, y)


if __name__ == '__main__':
    s = Spam(2)
    p = Proxy(s)
    print p.x
    print '-' * 20

    p.bar(3)
    print '-' * 20

    p.x = 7
    print p.x
