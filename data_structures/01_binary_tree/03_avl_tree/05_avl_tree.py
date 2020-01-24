# -*- coding: utf-8 -*-

'''
An auto-balanced binary tree!
平衡二叉搜索树
'''

import math
import random


class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def push(self, data):
        self.data.append(data)
        self.tail = self.tail + 1

    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    def count(self):
        return self.tail - self.head

    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])


class my_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getheight(self):
        return self.height

    def setdata(self, data):
        self.data = data
        return

    def setleft(self, node):
        self.left = node
        return

    def setright(self, node):
        self.right = node
        return

    def setheight(self, height):
        self.height = height
        return

    def __str__(self):
        left = self.getleft()
        right = self.getright()
        if left is None and right is None:
            return 'data: %s, left: %s, right: %s, height: %s' % (self.data, None, None, self.height)
        elif left is not None and right is None:
            return 'data: %s, left: %s, right: %s, height: %s' % (self.data, left.getdata(), None, self.height)
        elif left is None and right is not None:
            return 'data: %s, left: %s, right: %s, height: %s' % (self.data, None, right.getdata(), self.height)
        else:
            return 'data: %s, left: %s, right: %s, height: %s' % (self.data, left.getdata(), right.getdata(), self.height)


def getheight(node):
    if node is None:
        return 0
    return node.getheight()


def my_max(a, b):
    if a > b:
        return a
    return b


def leftrotation(node):
    r'''
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB

        7-2 node         6-2            6-2
        /               /  \            /  \
      6-2 ret          5-1 7-2         5-1 7-1
      /                    / \             / \
     5-1

    UB = unbalanced node
    '''
    print("left rotation node:", node.getdata())
    print(node)
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()), getheight(ret.getleft())) + 1
    ret.setheight(h2)
    return ret


def rightrotation(node):
    r'''
        a mirror symmetry rotation of the leftrotation

    7-2 node           8-2             8-2
      \               /   \            / \
      8-2 ret        7-2  9-1        7-1  9-1
        \            / \
        9-1

    '''
    print("right rotation node:", node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()), getheight(ret.getleft())) + 1
    ret.setheight(h2)
    return ret


def rlrotation(node):
    r'''
            A              A                    Br
           / \            / \                  /  \
          B   C    RR    Br  C       LR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C
             \        /
             UB     Bl
    RR = rightrotation   LR = leftrotation
    '''
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)


def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)


def insert_node(node, data):
    print('&&&&& node: %s' % node)
    print('&&&&& data: %s' % data)
    if node is None:
        return my_node(data)
    if data < node.getdata():
        print('node.getleft(): %s' % node.getleft())
        node.setleft(insert_node(node.getleft(), data))
        print('node.getleft(): %s' % node.getleft())
        print('getheight(node.getleft()): %s' % getheight(node.getleft()))
        print('node.getright(): %s' % node.getright())
        print('getheight(node.getright()): %s'% getheight(node.getright()))
        if getheight(node.getleft()) - getheight(node.getright()) == 2:  # an unbalance detected
            r"""
               10 node                 10  node
              /                       /  \
             6                       6   18
            / \                    /   \
                 data             2     8
                                 / \   / \
                                1   3  7  9 data
            """
            if data < node.getleft().getdata():  # new node is the left child of the left child
                node = leftrotation(node)
            else:
                node = rlrotation(node)  # new node is the right child of the left child
    else:
        print('node.getright(): %s' % node.getright())
        node.setright(insert_node(node.getright(), data))
        print('node.getright(): %s' % node.getright())
        print('getheight(node.getright()): %s' % getheight(node.getright()))
        print('node.getleft(): %s' % node.getleft())
        print('getheight(node.getleft()): %s' % getheight(node.getleft()))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            r"""
             7   node                     10  node
              \                          /  \
               8                        6   18
              / \                         /     \
                   data                  12     22
                                        / \     / \
                                       11 13   19 25 data
            """
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)
    return node


def getRightMost(root):
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()


def getLeftMost(root):
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()


def del_node(root, data):
    print('&&&&& root: %s' % root)
    print('&&&&& data: %s' % data)

    if data == root.getdata():
        print('data == root.getdata()')
        """
        left     | right
        ---------|---------
        not None | not None
        not None | None
        None     | not None
        None     | None
        """
        if root.getleft() is not None and root.getright() is not None:
            print('root.getleft() is not None and root.getright() is not None')
            temp_data = getLeftMost(root.getright())
            print('temp_data: %s' % temp_data)
            root.setdata(temp_data)
            print('root: %s' % root)
            root.setright(del_node(root.getright(), temp_data))
        elif root.getleft() is not None:
            print('root.getleft() is not None')
            print('root = root.getleft()')
            root = root.getleft()
        else:
            print('root.getright() is not None or (None, None)')
            print('root = root.getright()')
            root = root.getright()

    elif data < root.getdata():
        print('data < root.getdata()')
        if root.getleft() is None:
            print("No such data")
            return root
        else:
            root.setleft(del_node(root.getleft(), data))

    elif data > root.getdata():
        print('data > root.getdata()')
        if root.getright() is None:
            return root
        else:
            root.setright(del_node(root.getright(), data))

    if root is None:
        return root

    r"""
     6           6           6      6
      \           \           \      \
       9  =>       9           9      9
     /  \           \         /      / \
     8  10           10      8       8 10
     
         6             6        6           6
        /             /        /           /
       3   =>        3        3           3
      / \           /          \         / \
     2   5         2            5       2   5
    """
    if getheight(root.getright()) - getheight(root.getleft()) == 2:
        if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
            root = rightrotation(root)
        else:
            root = lrrotation(root)
    elif getheight(root.getright()) - getheight(root.getleft()) == -2:
        if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
            root = leftrotation(root)
        else:
            root = rlrotation(root)

    height = my_max(getheight(root.getright()), getheight(root.getleft())) + 1
    root.setheight(height)
    return root


class AVLtree:
    def __init__(self):
        self.root = None

    def getheight(self):
        #        print("yyy")
        return getheight(self.root)

    def insert(self, data):
        print("insert:" + str(data))
        self.root = insert_node(self.root, data)

    def del_node(self, data):
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root, data)

    def traversale(self):  # a level traversale, gives a more intuitive look on the tree
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        if layer == 0:
            return
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            print(space, end="")
            if node is None:
                print("*", end="")
                q.push(None)
                q.push(None)
            else:
                print(node.getdata(), end="")
                q.push(node.getleft())
                q.push(node.getright())
            print(space, end="")
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        print()
                        print("*************************************")
                        return
                    print()
                    break
        print()
        print("*************************************")
        return

    def test(self):
        getheight(None)
        print("****")
        self.getheight()


if __name__ == "__main__":
    t = AVLtree()
    t.traversale()
    l = [4, 2, 7, 6, 3, 5, 8, 0, 9, 1]
    print(l)
    for i in l:
        t.insert(i)
        t.traversale()
    print()
    print()
    print()
    for i in l:
        t.del_node(i)
        t.traversale()

r"""
% python3 05_avl_tree.py
[4, 2, 7, 6, 3, 5, 8, 0, 9, 1]
insert:4
&&&&& node: None
&&&&& data: 4
 4
 
    4-1
  /    \
 None None
*************************************
insert:2
&&&&& node: data: 4, left: None, right: None, height: 1
&&&&& data: 2
node.getleft(): None
&&&&& node: None
&&&&& data: 2
node.getleft(): data: 2, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): None
getheight(node.getright()): 0
  4
 2  *

    4-2
  /    \
 2-1   None
*************************************
insert:7
&&&&& node: data: 4, left: 2, right: None, height: 2
&&&&& data: 7
node.getright(): None
&&&&& node: None
&&&&& data: 7
node.getright(): data: 7, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): data: 2, left: None, right: None, height: 1
getheight(node.getleft()): 1
  4
 2  7

    4-2
  /    \
 2-1   7-1
*************************************
insert:6
&&&&& node: data: 4, left: 2, right: 7, height: 2
&&&&& data: 6
node.getright(): data: 7, left: None, right: None, height: 1
&&&&& node: data: 7, left: None, right: None, height: 1
&&&&& data: 6
node.getleft(): None
&&&&& node: None
&&&&& data: 6
node.getleft(): data: 6, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): None
getheight(node.getright()): 0
node.getright(): data: 7, left: 6, right: None, height: 2
getheight(node.getright()): 2
node.getleft(): data: 2, left: None, right: None, height: 1
getheight(node.getleft()): 1
    4
  2    7
 *  *  6  *
 
    4-3
  /    \
 2-1   7-2
       /
      6-1

*************************************
insert:3
&&&&& node: data: 4, left: 2, right: 7, height: 3
&&&&& data: 3
node.getleft(): data: 2, left: None, right: None, height: 1
&&&&& node: data: 2, left: None, right: None, height: 1
&&&&& data: 3
node.getright(): None
&&&&& node: None
&&&&& data: 3
node.getright(): data: 3, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): None
getheight(node.getleft()): 0
node.getleft(): data: 2, left: None, right: 3, height: 2
getheight(node.getleft()): 2
node.getright(): data: 7, left: 6, right: None, height: 2
getheight(node.getright()): 2
    4
  2    7
 *  3  6  *

    4-3
  /    \
 2-2   7-2
  \     /
  3-1  6-1

*************************************
insert:5
&&&&& node: data: 4, left: 2, right: 7, height: 3
&&&&& data: 5
node.getright(): data: 7, left: 6, right: None, height: 2
&&&&& node: data: 7, left: 6, right: None, height: 2
&&&&& data: 5
node.getleft(): data: 6, left: None, right: None, height: 1
&&&&& node: data: 6, left: None, right: None, height: 1
&&&&& data: 5
node.getleft(): None
&&&&& node: None
&&&&& data: 5
node.getleft(): data: 5, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): None
getheight(node.getright()): 0
node.getleft(): data: 6, left: 5, right: None, height: 2
getheight(node.getleft()): 2
node.getright(): None
getheight(node.getright()): 0
left rotation node: 7
data: 7, left: 6, right: None, height: 2
node.getright(): data: 6, left: 5, right: 7, height: 2
getheight(node.getright()): 2
node.getleft(): data: 2, left: None, right: 3, height: 2
getheight(node.getleft()): 2
    4
  2    6
 *  3  5  7

    4-3
  /    \
 2-2   7-2
  \     /
  3-1  6-2
        /
      5-1

     6-2      6-2
    /   \    /   \
   5-1 7-2  5-1 7-1

      4-3
    /     \
   2-2    6-2
    \     /  \
    3-1  5-1 7-1
*************************************
insert:8
&&&&& node: data: 4, left: 2, right: 6, height: 3
&&&&& data: 8
node.getright(): data: 6, left: 5, right: 7, height: 2
&&&&& node: data: 6, left: 5, right: 7, height: 2
&&&&& data: 8
node.getright(): data: 7, left: None, right: None, height: 1
&&&&& node: data: 7, left: None, right: None, height: 1
&&&&& data: 8
node.getright(): None
&&&&& node: None
&&&&& data: 8
node.getright(): data: 8, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): None
getheight(node.getleft()): 0
node.getright(): data: 7, left: None, right: 8, height: 2
getheight(node.getright()): 2
node.getleft(): data: 5, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): data: 6, left: 5, right: 7, height: 3
getheight(node.getright()): 3
node.getleft(): data: 2, left: None, right: 3, height: 2
getheight(node.getleft()): 2
        4
    2        6
  *    3    5    7
 *  *  *  *  *  *  *  8

      4-4
    /     \
   2-2    6-3
    \     /  \
    3-1  5-1 7-2
              \
              8-1

*************************************
insert:0
&&&&& node: data: 4, left: 2, right: 6, height: 4
&&&&& data: 0
node.getleft(): data: 2, left: None, right: 3, height: 2
&&&&& node: data: 2, left: None, right: 3, height: 2
&&&&& data: 0
node.getleft(): None
&&&&& node: None
&&&&& data: 0
node.getleft(): data: 0, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): data: 3, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): data: 2, left: 0, right: 3, height: 2
getheight(node.getleft()): 2
node.getright(): data: 6, left: 5, right: 7, height: 3
getheight(node.getright()): 3
        4
    2        6
  0    3    5    7
 *  *  *  *  *  *  *  8

        4-4
      /      \
     2-2     6-3
    /   \    /  \
  0-1  3-1  5-1 7-2
                 \
                8-1

*************************************
insert:9
&&&&& node: data: 4, left: 2, right: 6, height: 4
&&&&& data: 9
node.getright(): data: 6, left: 5, right: 7, height: 3
&&&&& node: data: 6, left: 5, right: 7, height: 3
&&&&& data: 9
node.getright(): data: 7, left: None, right: 8, height: 2
&&&&& node: data: 7, left: None, right: 8, height: 2
&&&&& data: 9
node.getright(): data: 8, left: None, right: None, height: 1
&&&&& node: data: 8, left: None, right: None, height: 1
&&&&& data: 9
node.getright(): None
&&&&& node: None
&&&&& data: 9
node.getright(): data: 9, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): None
getheight(node.getleft()): 0
node.getright(): data: 8, left: None, right: 9, height: 2
getheight(node.getright()): 2
node.getleft(): None
getheight(node.getleft()): 0
right rotation node: 7
node.getright(): data: 8, left: 7, right: 9, height: 2
getheight(node.getright()): 2
node.getleft(): data: 5, left: None, right: None, height: 1
getheight(node.getleft()): 1
node.getright(): data: 6, left: 5, right: 8, height: 3
getheight(node.getright()): 3
node.getleft(): data: 2, left: 0, right: 3, height: 2
getheight(node.getleft()): 2
        4
    2        6
  0    3    5    8
 *  *  *  *  *  *  7  9

        4-4
      /      \
     2-2     6-3
    /   \    /  \
  0-1  3-1  5-1 7-2
                 \
                 8-2
                  \
                  9-1

      8-2       8-2
     /  \      /  \
   7-2  9-1  7-1  9-1
   
           4-4
        /       \
      2-2      6-3
     /  \    /    \
   0-1 3-1  5-1   8-2
                  / \
                7-1 9-1

*************************************
insert:1
&&&&& node: data: 4, left: 2, right: 6, height: 4
&&&&& data: 1
node.getleft(): data: 2, left: 0, right: 3, height: 2
&&&&& node: data: 2, left: 0, right: 3, height: 2
&&&&& data: 1
node.getleft(): data: 0, left: None, right: None, height: 1
&&&&& node: data: 0, left: None, right: None, height: 1
&&&&& data: 1
node.getright(): None
&&&&& node: None
&&&&& data: 1
node.getright(): data: 1, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): None
getheight(node.getleft()): 0
node.getleft(): data: 0, left: None, right: 1, height: 2
getheight(node.getleft()): 2
node.getright(): data: 3, left: None, right: None, height: 1
getheight(node.getright()): 1
node.getleft(): data: 2, left: 0, right: 3, height: 3
getheight(node.getleft()): 3
node.getright(): data: 6, left: 5, right: 8, height: 3
getheight(node.getright()): 3
        4
    2        6
  0    3    5    8
 *  1  *  *  *  *  7  9

           4-4
        /       \
      2-3      6-3
     /  \    /    \
   0-2 3-1  5-1   8-2
    \             / \
    1-1         7-1 9-1

*************************************











           4-4
        /       \
      2-3      6-3
     /  \    /    \
   0-2 3-1  5-1   8-2
    \             / \
    1-1         7-1 9-1

delete:4
&&&&& root: data: 4, left: 2, right: 6, height: 4
&&&&& data: 4
data == root.getdata()
root.getleft() is not None and root.getright() is not None
temp_data: 5
root: data: 5, left: 2, right: 6, height: 4

           5-4
        /       \
      2-3      6-3
     /  \    /    \
   0-2 3-1  5-1   8-2
    \             / \
    1-1         7-1 9-1

&&&&& root: data: 6, left: 5, right: 8, height: 3
&&&&& data: 5
data < root.getdata()
&&&&& root: data: 5, left: None, right: None, height: 1
&&&&& data: 5
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()

           5-4
        /       \
      2-3      6-3
     /  \         \
   0-2 3-1        8-2
    \             / \
    1-1         7-1 9-1

    7-3         6-3           7-3
     \           \           /   \
     8-2         7-3        6-1 8-2
       \          \              \
       9-1        8-2            9-1
                    \
                    9-1
                    
left rotation node: 8
data: 8, left: 7, right: 9, height: 2
right rotation node: 6

             5-4
           /     \
         2-3     7-3
        /  \     /  \
      0-2 3-1   6-1 8-2
       \             \
       1-1           9-1  


        5
    2        7
  0    3    6    8
 *  1  *  *  *  *  *  9
*************************************

             5-4
           /     \
         2-3     7-3
        /  \     /  \
      0-2 3-1   6-1 8-2
       \             \
       1-1           9-1  


delete:2
&&&&& root: data: 5, left: 2, right: 7, height: 4
&&&&& data: 2
data < root.getdata()
&&&&& root: data: 2, left: 0, right: 3, height: 3
&&&&& data: 2
data == root.getdata()
root.getleft() is not None and root.getright() is not None
temp_data: 3
root: data: 3, left: 0, right: 3, height: 3

             5-4
           /     \
         3-3     7-3
        /  \     /  \
      0-2 3-1   6-1 8-2
       \             \
       1-1           9-1  


&&&&& root: data: 3, left: None, right: None, height: 1
&&&&& data: 3
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()

             5-4
           /     \
         3-3     7-3
        /        /  \
      0-2      6-1 8-2
       \             \
       1-1           9-1  

   1-2       3-3    1-2
   /         /      /  \
  0-1      1-2     0-1 3-1
            /
          0-1
  
         5-4
     /        \
    1-2      7-3
   /   \    /  \
  0-1 3-1  6-1 8-2
                \
                9-1
  
right rotation node: 0
left rotation node: 3
data: 3, left: 1, right: None, height: 3
        5
    1        7
  0    3    6    8
 *  *  *  *  *  *  *  9
*************************************

         5-4
     /        \
    1-2      7-3
   /   \    /  \
  0-1 3-1  6-1 8-2
                \
                9-1

delete:7
&&&&& root: data: 5, left: 1, right: 7, height: 4
&&&&& data: 7
data > root.getdata()
&&&&& root: data: 7, left: 6, right: 8, height: 3
&&&&& data: 7
data == root.getdata()
root.getleft() is not None and root.getright() is not None
temp_data: 8
root: data: 8, left: 6, right: 8, height: 3

         5-4
     /        \
    1-2      8-3
   /   \    /  \
  0-1 3-1  6-1 8-2
                \
                9-1

&&&&& root: data: 8, left: None, right: 9, height: 2
&&&&& data: 8
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()

         5-3
     /        \
    1-2      8-2
   /   \    /  \
  0-1 3-1  6-1 9-1


    5
  1    8
 0  3  6  9
*************************************

         5-3
     /        \
    1-2      8-2
   /   \    /  \
  0-1 3-1  6-1 9-1

delete:6
&&&&& root: data: 5, left: 1, right: 8, height: 3
&&&&& data: 6
data > root.getdata()
&&&&& root: data: 8, left: 6, right: 9, height: 2
&&&&& data: 6
data < root.getdata()
&&&&& root: data: 6, left: None, right: None, height: 1
&&&&& data: 6
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()
    5
  1    8
 0  3  *  9
*************************************

         5-3
     /        \
    1-2      8-2
   /   \       \
  0-1 3-1      9-1

delete:3
&&&&& root: data: 5, left: 1, right: 8, height: 3
&&&&& data: 3
data < root.getdata()
&&&&& root: data: 1, left: 0, right: 3, height: 2
&&&&& data: 3
data > root.getdata()
&&&&& root: data: 3, left: None, right: None, height: 1
&&&&& data: 3
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()
    5
  1    8
 0  *  *  9
*************************************

         5-3
     /        \
    1-2      8-2
   /           \
  0-1         9-1


delete:5
&&&&& root: data: 5, left: 1, right: 8, height: 3
&&&&& data: 5
data == root.getdata()
root.getleft() is not None and root.getright() is not None
temp_data: 8
root: data: 8, left: 1, right: 8, height: 3

         8-3
     /        \
    1-2      8-2
   /           \
  0-1         9-1


&&&&& root: data: 8, left: None, right: 9, height: 2
&&&&& data: 8
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()

         8-3
     /        \
    1-2      9-1
   /           
  0-1         


    8
  1    9
 0  *  *  *
*************************************

         8-3
     /        \
    1-2      9-1
   /           
  0-1         


delete:8
&&&&& root: data: 8, left: 1, right: 9, height: 3
&&&&& data: 8
data == root.getdata()
root.getleft() is not None and root.getright() is not None
temp_data: 9
root: data: 9, left: 1, right: 9, height: 3

         9-3
     /        \
    1-2      9-1
   /           
  0-1         


&&&&& root: data: 9, left: None, right: None, height: 1
&&&&& data: 9
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()

    9-3
     /        
    1-2      
   /           
  0-1         

left rotation node: 9
data: 9, left: 1, right: None, height: 3
  1
 0  9
*************************************

     1-2
    /  \
   0-1 9-1

delete:0
&&&&& root: data: 1, left: 0, right: 9, height: 2
&&&&& data: 0
data < root.getdata()
&&&&& root: data: 0, left: None, right: None, height: 1
&&&&& data: 0
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()
  1
 *  9
*************************************
delete:9
&&&&& root: data: 1, left: None, right: 9, height: 2
&&&&& data: 9
data > root.getdata()
&&&&& root: data: 9, left: None, right: None, height: 1
&&&&& data: 9
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()
 1
*************************************
delete:1
&&&&& root: data: 1, left: None, right: None, height: 1
&&&&& data: 1
data == root.getdata()
root.getright() is not None or (None, None)
root = root.getright()




"""