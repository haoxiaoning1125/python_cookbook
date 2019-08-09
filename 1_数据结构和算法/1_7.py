# coding:utf-8

"""
字典排序
在迭代操作的时候保持元素被插入时的顺序
一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表
"""

from collections import OrderedDict
import json

if __name__ == '__main__':
    od = OrderedDict()
    od['foo'] = 1
    od['bar'] = 2
    od['spam'] = 3
    od['grok'] = 4
    for k, v in od.items():
        print (k, v)

    print json.dumps(od)
