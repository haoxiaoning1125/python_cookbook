# coding:utf-8

"""
在一个序列上面保持元素顺序的同时消除重复的值
"""


def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    # 序列上的值都是 hashable 类型
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print list(dedupe1(a))
    print '-' * 20

    # 序列上存在不可哈希的元素
    b = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 4}
    ]
    print list(dedupe2(b, key=lambda x: (x['x'], x['y'])))
    print list(dedupe2(b, key=lambda x: x['x']))
    print '-' * 20

    # set, 去重但打乱顺序
    print set(a)
