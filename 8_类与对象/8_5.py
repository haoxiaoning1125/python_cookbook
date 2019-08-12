# coding:utf-8

"""
在类中封装属性名
"""


class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


if __name__ == '__main__':
    pass
