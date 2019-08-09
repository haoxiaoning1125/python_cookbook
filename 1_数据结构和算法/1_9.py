# coding:utf-8

"""
在两字典的 keys() 或者 items() 方法返回结果上执行集合操作
"""

if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print set(a.keys()) & set(b.keys())
    print set(a.keys()) - set(b.keys())
    print set(a.items()) & set(b.items())
    print '-' * 20

    # 从现有字典构造新字典
    c = {key: a[key] for key in set(a.keys()) - {'z', 'w'}}
    print c
