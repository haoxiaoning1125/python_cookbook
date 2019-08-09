# coding:utf-8

"""
手动遍历迭代器
"""


def manual_iter():
    with open('python_cookbook/files/4_1.txt.txt') as f:
        try:
            i = 0
            while True:
                line = next(f)
                print 'line{}: {}'.format(i, line)
        except StopIteration as e:
            print e.message
    f.close()


if __name__ == '__main__':
    # manual_iter()
    pass