"""自定义同步原语
外界的操作唤醒所有处于阻塞状态的线程
"""

import threading
import time


class Channel:
    """封装内置的 Barrier 同步原语"""
    def __init__(self, n):
        self.barrier = threading.Barrier(n)

    def send(self):
        self.barrier.abort()

    def receive(self):
        self.barrier.wait()


class Barrier:
    """实现阻塞状态的线程数达到一定数量后唤醒所有线程的同步原语"""
    def __init__(self, n):
        self.channel = Channel(n)

    def abort(self):
        """调用该方法后将中止所有线程的异常状态"""
        self.channel.send()

    def wait(self):
        """调用该方法后线程处于阻塞状态，直到阻塞线程数量达到规定数量"""
        self.channel.receive()


def worker(barrier):
    print('{} waiting for barrier before'.format(threading.current_thread().name))
    try:
        barrier.wait()
    except:
        print('{} waiting for barrier after'.format(threading.current_thread().name))
    else:
        print('{} waiting for barrier after'.format(threading.current_thread().name))


if __name__ == '__main__':
    num_threads = 3
    barrier = Barrier(num_threads + 1)

    threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(num_threads)
    ]

    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    barrier.abort()  # 中止线程的阻塞状态

    for t in threads:
        t.join()
