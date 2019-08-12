# coding:utf-8

"""
在子类中扩展定义在父类中的 property 的功能
"""

class Person:
    def __init__(self, name):
        self.name = name

    # getter
    @property
    def name(self):
        return self.name

    # setter
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.name = value

    # deleter
    @name.deleter
    def name(self):
        raise AttributeError('Can\'t delete attribute')


class SubPerson(Person):
    # getter
    @property
    def name(self):
        print 'getting name'
        return super(SubPerson, self).name()

    # setter
    @name.setter
    def name(self, value):
        print 'setting name'
        super(SubPerson, self).name.__set__(self, value)

    # deleter
    @name.deleter
    def name(self):
        print 'deleting name'
        super(SubPerson, self).name.__delete__(self)

if __name__ == '__main__':
    s = SubPerson('a')
    print s.name
    # s.name = 'b'
    # print s.name
    # del s.name
    # print s.name