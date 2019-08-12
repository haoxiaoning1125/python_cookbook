# coding:utf-8

"""
创建可管理的属性
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    # getter
    @property
    def first_name(self):
        return self.first_name

    # setter
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.first_name = value

    # deleter
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can\'t delete attribute')


if __name__ == '__main__':
    a = Person('a')
    print a.first_name
    a.first_name = 'b'
    del a.first_name
    try:
        print a.first_name
    except Exception as e:
        print e.message

    print '-' * 20

    print Person.first_name.fget
    print Person.first_name.fset
    print Person.first_name.fdel
