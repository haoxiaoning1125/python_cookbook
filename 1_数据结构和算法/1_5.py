# coding:utf-8

"""
优先级队列
堆的值可以是元组类型，可以对带权值的元素进行排序
"""

import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # print len(self._queue)
        return heapq.heappop(self._queue)[-1]

    def get_index(self):
        return self._index


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print [q.pop() for _ in range(q.get_index())]
