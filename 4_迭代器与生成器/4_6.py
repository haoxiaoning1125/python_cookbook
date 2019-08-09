# coding:utf-8

"""
带有外部状态的生成器函数
"""


from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('4_6.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                print ['{}:{}'.format(lineno, hline) for lineno, hline in lines.history]
