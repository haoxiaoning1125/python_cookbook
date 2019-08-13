# coding:utf-8

"""
锁
"""

import threading
import time


class SharedCounter:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def get_value(self):
        return self._value

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta


class User:
    def __init__(self, data, mode, times):
        self._data = data
        self._mode = mode
        self._times = times

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        while self._times > 0:
            if self._mode == 1:
                self._data.incr(10)
            else:
                self._data.decr(10)
            print 'mode:{}, data:{}'.format(self._mode, self._data.get_value())
            time.sleep(1)
            self._times -= 1


if __name__ == '__main__':
    sc = SharedCounter(10)
    u1 = User(sc, 1, 10)
    u2 = User(sc, 0, 10)
    u1.start()
    u2.start()
