#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
try:
    import thread as thread
except ImportError:
    import _thread as thread
from abc import ABCMeta, abstractmethod

class Channel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def receive(self):
        pass


class Lock:
    """使用非缓冲通道实现 Lock 逻辑
    """
    def __init__(self):
        self.channel_acquire = Channel()  # 获取锁使用的通道
        self.channel_release = Channel()  # 释放锁使用的通道
        self.worker_running = True
        thread.start_new_thread(Lock.worker, (self, ))

    def worker(self):
        while self.worker_running:
            self.channel_acquire.receive()  # 接收获取锁时发送过来的数据，使获取锁之后可以继续执行
            self.channel_release.send(1)  # 向释放锁使用的通道发送数据，此时会阻塞，直到释放锁为止

    def acquire(self):
        """
        获取锁
        第一个成功向 channel_acquire 发送数据的线程将获取锁，
        其他线程因为无法再次接收数据而导致阻塞
        """
        self.channel_acquire.send(1)

    def release(self):
        """
        释放锁
        第一个获取锁的线程释放锁，也就是接收 channel_release 通道中的数据，
        此时可以继续从 channel_acquire 接收数据，其他线程获取到锁
        """
        self.channel_release.receive()

    def stop_worker(self):
        """
        因为锁的实现中启动了一个内部工作的线程，当锁使用完毕后需要停止该内部线程
        使用标志位直接让线程停止运行，有可能还需要关闭所有使用到的通道唤醒所有可能阻塞的线程
        """
        self.worker_running = False

    def __enter__(self):
        self.acquire()

    def __exit__(self, type, value, tb):
        self.release()

    def __del__(self):
        self.stop_worker()


class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.lock = Lock()
        self.channel = Channel()

    def wait(self):
        with self.lock:
            self.num_threads += 1
            if self.num_threads == self.n:
                for _ in range(self.n - 1):
                    self.channel.receive()
                    self.lock.stop_worker()
        if self.num_threads != self.n:  # 防止最后一个线程再次执行发送数据的操作
            self.channel.send(1)


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
