# coding:utf-8

"""
判断线程是否已经启动
"""


from threading import Thread, Event
import time


def countdown(n, started_evt):
    print 'countdown starting'
    started_evt.set()
    while n > 0:
        print ('T-minus', n)
        n -= 1
        time.sleep(0.5)


if __name__ == '__main__':
    started_evt = Event()
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()
    started_evt.wait()
    print('countdown is running')
