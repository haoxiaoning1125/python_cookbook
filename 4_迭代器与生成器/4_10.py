# coding:utf-8

"""
序列上索引值迭代
"""

if __name__ == '__main__':
    my_list = ['a', 'b', 'c']
    print [(idx, val) for idx, val in enumerate(my_list)]
    print [(idx, val) for idx, val in enumerate(my_list, 1)]
