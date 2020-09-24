#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

from abc import ABCMeta, abstractmethod

class Channel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def receive(self):
        pass

class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.channel = Channel()

    def worker(self):
        while True:
            if self.channel.receive():
                self.num_threads += 1
            if self.num_threads == self.n:
                break

    def wait(self):
        self.channel.send(1)  # 阻塞线程


def worker(barrier):
    print('{} waiting for barrier before'.format(threading.current_thread().name))
    barrier.wait()
    print('{} waiting for barrier after'.format(threading.current_thread().name))


if __name__ == '__main__':
    num_threads = 3
    barrier = Barrier(num_threads)

    threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(num_threads)
    ]

    for t in threads:
        print('{} starting'.format(t.name))
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()
