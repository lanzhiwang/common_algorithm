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

class SynchronizeChannel(Channel):
    """
    接口 Channel 的具体实现
    功能类似于 golng 的非缓冲通道
    """
    def __init__(self, n=0):
        self.semaphore = threading.Semaphore(n)

    def send(self, data=None):
        self.semaphore.acquire()

    def receive(self):
        self.semaphore.release()


class CustomizeLock():
    """
    使用 SynchronizeChannel 实现 lock 的类似功能
    功能上类似于 golang 中容量为 1 的通道
    """
    def __init__(self):
        self.sc = SynchronizeChannel(1)

    def acquire(self):
        """获取锁
        """
        self.sc.send()

    def release(self):
        """释放锁
        """
        self.sc.receive()

    def __enter__(self):
        self.acquire()

    def __exit__(self, type, value, tb):
        self.release()


class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.lock = CustomizeLock()
        self.sc = SynchronizeChannel(0)

    def wait(self):
        with self.lock:
            self.num_threads += 1

        if self.num_threads != self.n:
            self.sc.send()  # 阻塞线程
        else:
            for _ in range(self.n - 1):
                self.sc.receive()  # 唤醒所有线程


def worker(barrier):
    print('{} waiting for barrier before'.format(threading.current_thread().name))
    barrier.wait()
    print('{} waiting for barrier after'.format(threading.current_thread().name))


if __name__ == '__main__':
    num_threads = 10
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
