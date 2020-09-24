import threading
import time


class Barrier:
    def __init__(self, n):
        self.barrier = threading.Barrier(n)

    def wait(self):
        self.barrier.wait()


def worker(barrier):
    print('{} waiting for barrier before'.format(threading.current_thread().name))
    barrier.wait()
    print('{} waiting for barrier after'.format(threading.current_thread().name))

NUM_THREADS = 3

# barrier = threading.Barrier(NUM_THREADS)
barrier = Barrier(NUM_THREADS)

threads = [
    threading.Thread(
        name='worker-%s' % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'starting')
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()