# coding:utf-8

"""
合并多个字典或映射
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在
"""

# from collections import ChainMap  # python3..?
from pip._vendor.distlib.compat import ChainMap  # python2

if __name__ == '__main__':
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    c = ChainMap(a, b)  # 出现重复 key, 第一次出现的映射值被返回
    print(c['x'])  # Outputs 1 (from a)
    print(c['y'])  # Outputs 2 (from b)
    print(c['z'])  # Outputs 3 (from a)

    print len(c)
    print list(c.keys())
    print list(c.values())

    # 使用 update 代替 ChainMap
    # 创建一个完全不同的字典对象 (或者是破坏现有字典结构)
    # 如果原字典做了更新，这种改变不会反应到新的合并字典中去
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = dict(b)
    merged.update(a)
    for k, v in merged.items():
        print (k, v)