# coding:utf-8

"""
使用延迟计算属性
"""


import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print 'computing area'
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print 'computing perimeter'
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print c.radius
    print c.area()
