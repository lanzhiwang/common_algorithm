#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

"""

"""

class Channel:
    def __init__(self, chan=[]):
        self.chan = chan

    def send(self, data):
        self.chan.append(data)

    def receive(self):
        data = None
        try:
            data = self.chan.pop(0)
        except IndexError:
            pass
        return data


class Barrier:
    def __init__(self, n):
        self.n = n
        self.channel = Channel()

    def send(self):
        for _ in range(self.n-1):
            time.sleep(1)
            self.channel.send(1)

    def wait(self):
        if self.channel.receive() is None:
            return True
        else:
            return False


def send_work(barrier):
    print('%s - %s' % (threading.current_thread().getName(), 'send'))
    barrier.send()

    # for _ in range(count):
    #     time.sleep(1)
    #     chan.send(1)

def receive_work(barrier):
    print('%s - %s' % (threading.current_thread().getName(), 'before'))
    while barrier.wait():
        time.sleep(2)
    else:
        print('%s - %s' % (threading.current_thread().getName(), 'after'))

    # while chan.receive() is None:
    #     time.sleep(2)
    # else:
    #     print('%s - %s' % (threading.current_thread().getName(), 'after'))






if __name__ == '__main__':
    barrier = Barrier(3)
    receive1 = threading.Thread(name='receive_work1', target=receive_work, args=(barrier,))
    receive2 = threading.Thread(name='receive_work2', target=receive_work, args=(barrier,))

    send = threading.Thread(name='send_work', target=send_work, args=(barrier,))

    receive1.start()
    receive2.start()
    time.sleep(4)
    send.start()

