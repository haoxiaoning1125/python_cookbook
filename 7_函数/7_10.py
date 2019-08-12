# coding:utf-8

"""
带额外状态信息的回调函数
"""


def apply_async(func, callback, *args):
    result = func(*args)
    callback(result)


def print_result(result):
    print ('Got: {}'.format(result))


def add(x, y):
    return x + y


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print ('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print ('[{}] Got: {}'.format(sequence, result))


if __name__ == '__main__':
    apply_async(add, print_result, 1, 2)
    apply_async(add, print_result, 'hello', ' world')
    print '-' * 20

    rh = ResultHandler()
    for i in range(3):
        apply_async(add, rh.handler, 'a', 'b')
    print '-' * 20

    handler = make_handler()
    next(handler)
    # apply_async(add, handler.send(), 'war', 'frame')
