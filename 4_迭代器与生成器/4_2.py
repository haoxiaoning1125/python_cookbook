# coding:utf-8

"""
代理迭代
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._child = []

    def __repr__(self):
        return 'Node:value=({!r})'.format(self._value)

    def add_child(self, node):
        self._child.append(node)

    def __iter__(self):
        return iter(self._child)


if __name__ == '__main__':
    root = Node(0)
    cs = [Node(1), Node(2)]
    for c in cs:
        root.add_child(c)
    print [c for c in root]
