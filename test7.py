#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

class Channel:
    def __init__(self):
        """模拟 golang 中的非缓冲通道，当没有接收线程时一直处于阻塞状态，直到有线程开始接收数据
        Event 相当于非缓冲通道
        Event.wait 相当于向非缓冲通道发送数据，此时如果没有接收者就会阻塞线程
        Event.set 相当于向非缓冲通道接收数据，使之前发送数据阻塞的线程恢复
        """
        self.e = threading.Event()
        self.lock = threading.Lock()

    def send(self, data):
        """发送数据时，阻塞所有线程，直到有线程开始接收数据
        """
        with self.lock:
            data.num_threads += 1
        self.e.wait()

    def receive(self):
        """接收数据时将 Event 内部标志设置为 True, 唤醒所有阻塞的线程
        """
        self.e.set()


class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.channel = Channel()

    def wait(self):
        if self.num_threads != self.n - 1:
            self.channel.send(self)  # 阻塞线程
        else:
            self.channel.receive()  # 唤醒线程


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
