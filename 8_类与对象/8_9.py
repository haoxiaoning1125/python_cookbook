# coding:utf-8

"""
创建一个新的拥有一些额外功能的实例属性类型
"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 3)
    print p.x, p.y

    p.x = 5
    p.y = 2.3

    print p.x, p.y
