# coding:utf-8

"""
启动与停止线程
"""
import socket
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print ('T-minus', n)
        n -= 1
        time.sleep(0.5)


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print ('T-minus', n)
            n -= 1
            time.sleep(0.5)


class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
        return


if __name__ == '__main__':
    t = Thread(target=countdown, args=(3,))
    t.start()

    # c = CountdownTask()
    # t = Thread(target=c.run, args=(10,))
    # t.start()
    # c.terminate()
    # t.join()
