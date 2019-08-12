# coding:utf-8

"""
定义匿名或内联函数
"""

if __name__ == '__main__':
    add = lambda x, y: x + y
    print add(1, 2)
    print add('hello', 'world')

    names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    print sorted(names, key=lambda name: name.split()[-1].lower())


