import threading
import time
from abc import ABCMeta, abstractmethod

try:
    import thread as thread
except ImportError:
    import _thread as thread


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
        self.channel_acquire = Channel()
        self.channel_release = Channel()
        self.worker_running = True
        thread.start_new_thread(Lock.worker, (self, ))

    def worker(self):
        while self.worker_running:
            self.channel_acquire.receive()
            self.channel_release.send(1)

    def acquire(self):
        self.channel_acquire.send(1)

    def release(self):
        self.channel_release.receive()

    def __enter__(self):
        self.acquire()

    def __exit__(self, t, v, tb):
        self.release()

    def clean(self):
        self.worker_running = False


class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.lock = Lock()
        self._waiters = []

    def wait(self):
        """
        模拟 condition 同步原语

        thread1:                       thread2:                       thread3:
        lock.acquire()                 lock.acquire()                 lock.acquire()
        self.num_threads += 1          self.num_threads += 1          self.num_threads += 1

        waiter = Lock()                waiter = Lock()                for waiter in _waiters:
        waiter.acquire()               waiter.acquire()                   waiter.release()
        _waiters.append(waiter)        _waiters.append(waiter)
        lock.release()                 lock.release()
        waiter.acquire()  # 阻塞        waiter.acquire()  # 阻塞
        lock.acquire()                 lock.acquire()

        lock.release()                 lock.release()                 lock.release()
        """
        self.lock.acquire()
        self.num_threads += 1

        if self.num_threads == self.n:
            for waiter in self._waiters:
                waiter.release()
        else:
            waiter = Lock()
            waiter.acquire()
            self._waiters.append(waiter)
            self.lock.release()
            waiter.acquire()
            self.lock.acquire()

        self.lock.release()

    def clean(self):
        self.lock.clean()

    def __enter__(self):
        pass

    def __exit__(self, t, v, tb):
        self.clean()


def worker(barrier):
    print('{} waiting for barrier before'.format(threading.current_thread().name))
    barrier.wait()
    print('{} waiting for barrier after'.format(threading.current_thread().name))


if __name__ == '__main__':
    num_threads = 10
    barrier = Barrier(num_threads)

    with barrier:
        threads = []
        for i in range(num_threads):
            threads.append(threading.Thread(
                name='worker-%s' % i,
                target=worker,
                args=(barrier,),
            ))

        for t in threads:
            print('{} starting'.format(t.name))
            t.start()
            time.sleep(0.1)

        for t in threads:
            t.join()
