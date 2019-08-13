# coding:utf-8

"""
多个线程队列轮询
"""

import Queue
import socket
import os


class PollableQueue(Queue.Queue):
    def __init__(self):
        super(PollableQueue, self).__init__()
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.sockerpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        super(PollableQueue, self).put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super(PollableQueue, self).get()


if __name__ == '__main__':
    pass
