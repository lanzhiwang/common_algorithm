import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

class Barrier:
    def __init__(self, n):
        self.n = n  # 规定的线程数量
        self.num_threads = 0  # 活动的线程数量
        self.cv = threading.Condition()

    def wait(self):
        self.cv.acquire()

        logging.debug(self.num_threads)
        self.num_threads += 1
        logging.debug(self.num_threads)

        if self.num_threads == self.n:
            self.cv.notify_all()
        else:
            self.cv.wait()

        self.cv.release()

        """
        lock1.acquire()                lock1.acquire()                lock1.acquire()
        self.num_threads += 1          self.num_threads += 1          self.num_threads += 1

        waiter = Lock()                waiter = Lock()                for waiter in _waiters:
        waiter.acquire()               waiter.acquire()                   waiter.release()
        _waiters.append(waiter)        _waiters.append(waiter)
        lock1.release()                lock1.release()
        waiter.acquire()  # 阻塞        waiter.acquire()  # 阻塞
        lock1.acquire()                lock1.acquire()

        lock1.release()                lock1.release()                lock1.release()
        """


def worker(barrier):
    logging.debug('{} waiting for barrier before'.format(threading.current_thread().name))
    barrier.wait()
    logging.debug('{} waiting for barrier after'.format(threading.current_thread().name))


if __name__ == '__main__':
    num_threads = 10
    barrier = Barrier(num_threads)

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

