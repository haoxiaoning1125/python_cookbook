# coding:utf-8

"""
自定义数据容器
"""


import collections


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def add(self, item):
        self._items.append(item)
        self._items = sorted(self._items)


if __name__ == '__main__':
    items = SortedItems([5, 1, 3])
    print list(items)
    print (items[0], items[-1])
    items.add(2)
    print list(items)
