# coding:utf-8

"""
消息发布/订阅模型
"""

from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for sc in self._subscribers:
            sc.send(msg)


if __name__ == '__main__':
    pass
