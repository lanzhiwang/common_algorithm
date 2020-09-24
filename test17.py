import time
import threading
from abc import ABCMeta, abstractmethod
from itertools import islice as _islice

try:
    import thread as thread
except ImportError:
    import _thread as thread

try:
    from _collections import deque as _deque
except ImportError:
    from collections import deque as _deque


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
        return self

    def release(self):
        self.channel_release.receive()

    def __enter__(self):
        self.acquire()

    def __exit__(self, t, v, tb):
        self.release()

    def clean(self):
        self.worker_running = False


class RLock:
    """使用 Lock 机制实现可重入锁 RLock"""
    def __init__(self):
        self._block = Lock()
        self._owner = None
        self._count = 0

    def acquire(self):
        # get the ‘thread identifier’ of the current thread.
        me = thread.get_ident()
        if self._owner == me:
            self._count += 1
            return 1
        rc = self._block.acquire()
        if rc:
            self._owner = me
            self._count = 1
        return rc

    def release(self):
        if self._owner != thread.get_ident():
            raise RuntimeError("cannot release un-acquired lock")
        self._count = count = self._count - 1
        if not count:
            self._owner = None
            self._block.release()

    def __enter__(self):
        self.acquire()

    def __exit__(self, t, v, tb):
        self.release()

    def clean(self):
        self._block.clean()

    # Internal methods used by condition variables

    def _acquire_restore(self, state):
        self._block.acquire()
        self._count, self._owner = state

    def _release_save(self):
        if self._count == 0:
            raise RuntimeError("cannot release un-acquired lock")
        count = self._count
        self._count = 0
        owner = self._owner
        self._owner = None
        self._block.release()
        return (count, owner)

    def _is_owned(self):
        return self._owner == thread.get_ident()


class Condition:
    """使用可重入锁 RLock 实现条件变量 Condition"""
    def __init__(self):
        self._lock = RLock
        self._waiters = _deque()

        self._release_save = self._lock._release_save
        self._acquire_restore = self._lock._acquire_restore
        self._is_owned = self._lock._is_owned

    def acquire(self):
        self._lock.acquire()

    def release(self):
        self._lock.release()

    def __enter__(self):
        return self.acquire()

    def __exit__(self, *args):
        return self.release()

    def wait(self):
        # 判断调用该方法的线程是否已经获取了锁
        if not self._is_owned(self._lock):
            raise RuntimeError("cannot wait on un-acquired lock")
        waiter = Lock()
        waiter.acquire()
        self._waiters.append(waiter)
        saved_state = self._release_save(self._lock)  # 释放 _lock 使其他线程可以获取到该锁
        try:
            waiter.acquire()  # 线程在这里再次被阻塞
            return True
        finally:
            self._acquire_restore(self._lock, saved_state)  # 方法返回之前再次获取 _lock 以便后续释放

    def notify(self, n=1):
        # 判断调用该方法的线程是否已经获取了锁
        if not self._is_owned(self._lock):
            raise RuntimeError("cannot notify on un-acquired lock")
        all_waiters = self._waiters
        waiters_to_notify = _deque(_islice(all_waiters, n))
        if not waiters_to_notify:
            return
        for waiter in waiters_to_notify:
            waiter.release()  # 释放所有被阻塞的线程
            try:
                all_waiters.remove(waiter)
            except ValueError:
                pass

    def notify_all(self):
        self.notify(len(self._waiters))

    def clean(self):
        self._lock.clean()
        for waiters in _deque(_islice(self._waiters, len(self._waiters))):
            waiters.clean()


class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.cv = Condition()

    def wait(self):
        self.cv.acquire()
        self.num_threads += 1

        if self.num_threads == self.n:
            self.cv.notify_all()
        else:
            self.cv.wait()

        self.cv.release()

    def clean(self):
        self.cv.clean()

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
