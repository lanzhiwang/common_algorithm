# -*- coding: utf-8 -*-

'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent'''


class Link:
    next = None
    previous = None

    def __init__(self, x):
        self.value = x

    def displayLink(self):
        print("{}".format(self.value), end=" ")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insertHead(self, x):
        """
        insertHead(1)
        insertHead(2)
        insertHead(3)
        insertHead(4)

        1 -p-> 2 -p-> 3 -p-> 4
          <-n-   <-n-   <-n-
        tail                 head

        """
        newLink = Link(x)
        if self.isEmpty() == True:
            self.tail = newLink
        else:
            self.head.previous = newLink
        newLink.next = self.head
        self.head = newLink

    def insertTail(self, x):
        """
        1 -p-> 2 -p-> 3 -p-> 4
          <-n-   <-n-   <-n-
        tail                 head

        insertTail(0)

        0 -p-> 1 -p-> 2 -p-> 3 -p-> 4
          <-n-  <-n-   <-n-   <-n-
        tail                       head

        """
        newLink = Link(x)
        newLink.next = None
        self.tail.next = newLink
        newLink.previous = self.tail
        self.tail = newLink

    def deleteHead(self):
        """
        0 -p-> 1 -p-> 2 -p-> 3 -p-> 4
          <-n-  <-n-   <-n-   <-n-
        tail                       head

        deleteHead()
        0 -p-> 1 -p-> 2 -p-> 3
          <-n-  <-n-   <-n-
        tail                 head

        ###########################

        o
        tail
        head

        """
        temp = self.head
        self.head = self.head.next
        self.head.previous = None
        if self.head is None:
            self.tail = None
        return temp

    def deleteTail(self):
        """
        0 -p-> 1 -p-> 2 -p-> 3 -p-> 4
          <-n-  <-n-   <-n-   <-n-
        tail                       head

        deleteTail()
        1 -p-> 2 -p-> 3 -p-> 4
          <-n-   <-n-   <-n-
        tail                 head

        ###########################

        o
        tail
        head

        """
        temp = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        return temp

    def delete(self, x):
        """
        0 -p-> 1 -p-> 2 -p-> 3 -p-> 4
          <-n-  <-n-   <-n-   <-n-
        tail                       head

        delete(2)

        """
        current = self.head

        while current.value != x:
            current = current.next

        if current == self.head:
            self.deleteHead()
        elif current == self.tail:
            self.deleteTail()
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

    def display(self):
        current = self.head
        while current != None:
            current.displayLink()
            current = current.next
        print()

