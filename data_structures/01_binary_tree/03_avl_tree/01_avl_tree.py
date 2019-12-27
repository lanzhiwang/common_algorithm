# -*- coding: utf-8 -*-
"""

"""


class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    """
    push(1)
    push(2)
    push(3)
    
    [1, 2, 3]
    head=0   tail=3
    """
    def push(self, data):
        self.data.append(data)
        self.tail = self.tail + 1

    """
    [1, 2, 3]
    head=0   tail=3
    
    [1, 2, 3]
    head=1 tail=3
    """
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    """
    [1, 2, 3]
    head=1 tail=3
    
    tail-head = 2
    """
    def count(self):
        return self.tail - self.head

    def isEmpty(self):
        return self.head == self.tail

    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])

