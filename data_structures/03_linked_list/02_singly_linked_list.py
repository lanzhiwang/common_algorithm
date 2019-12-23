# -*- coding: utf-8 -*-


class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class Linked_List:
    def __init__(self):
        self.Head = None  # Initialize Head to None

    def insert_head(self, data):
        """
        (1, None)
        ^

        (2, ->) (1, None)
        ^

        (3, ->) (2, ->) (1, None)
        ^
        """
        newNod = Node(data)    # create a new node
        if self.Head != None:
            newNod.next = self.Head     # link newNode to head
        self.Head = newNod    # make NewNode as Head

    def insert_tail(self, data):
        """
        (3, ->) (2, ->) (1, None)
        ^

        (3, ->) (2, ->) (1, ->) (6, None)
        ^

        (3, ->) (2, ->) (1, ->) (6, ->) (5, ->)
        ^

        """
        if self.Head is None:
            self.insert_head(data)    #If this is first node, call insert_head
        else:
            temp = self.Head
            while temp.next != None:    #traverse to last node
                temp = temp.next
            temp.next = Node(data)    #create node & link to tail

    def printList(self):  # print every node data
        tamp = self.Head
        while tamp is not None:
            print(tamp.data)
            tamp = tamp.next

    def delete_head(self):  # delete from head
        """
        (3, ->) (2, ->) (1, ->) (6, ->) (5, ->)
        ^

        (2, ->) (1, ->) (6, ->) (5, ->)
        ^
        (3, None)

        """
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        """
        (2, ->) (1, ->) (6, ->) (5, ->)
        ^


        """
        tamp = self.Head
        if self.Head != None:
            if self.Head.next is None:    # if Head is the only Node in the Linked List
                self.Head = None
            else:
                while tamp.next.next is not None:  # find the 2nd last element
                    tamp = tamp.next
                tamp.next, tamp = None, tamp.next    #(2nd last element).next = None and tamp = last element
        return tamp

    def isEmpty(self):
        return self.Head is None  # Return if Head is none

    def reverse(self):
        prev = None
        current = self.Head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.Head = prev


def main():
    A = Linked_List()

    print("Inserting 1st at Head")
    a1 = input()  # 1
    A.insert_head(a1)

    print("Inserting 2nd at Head")
    a2 = input()  # 2
    A.insert_head(a2)

    print("\nPrint List : ")
    A.printList()  # 2 1

    print("\nInserting 1st at Tail")
    a3 = input()  # 6
    A.insert_tail(a3)

    print("Inserting 2nd at Tail")
    a4 = input()  # 5
    A.insert_tail(a4)

    print("\nPrint List : ")
    A.printList()  # 2 1 6 5

    print("\nDelete Head")
    A.delete_head()

    print("Delete Tail")
    A.delete_tail()

    print("\nPrint List : ")
    A.printList()  # 1 6

    print("\nReverse Linked List")
    A.reverse()

    print("\nPrint List : ")
    A.printList()  # 6 1


if __name__ == '__main__':
    main()

"""
Inserting 1st at Head
1
Inserting 2nd at Head
2

Print List :
2
1

Inserting 1st at Tail
6
Inserting 2nd at Tail
5

Print List :
2
1
6
5

Delete Head
Delete Tail

Print List :
1
6

Reverse Linked List

Print List :
6
1
"""