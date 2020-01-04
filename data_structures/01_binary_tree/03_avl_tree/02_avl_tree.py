# -*- coding: utf-8 -*-
"""
https://www.cnblogs.com/vamei/archive/2013/03/21/2964092.html
https://www.cnblogs.com/suimeng/p/4560056.html
"""


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

    UB = unbalanced node

    node = A
    ret = B

             A-4                        B-3
           /     \                    /     \
          B-3   C-3                  Bl-2    A-4
         /   \              -->     /      /    \
        Bl-2  Br-2                 UB-1   Br-2  C-3
       /
     UB-1

    '''
    print("left rotation node:", node.getdata())
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
        A                      C
       / \                    / \
      B   C                  A   Cr
         / \       -->      / \   \
        Cl  Cr             B  Cl  UB
             \
             UB

    UB = unbalanced node

    node = A
    ret = C
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

    node = A
    '''

    # b = node.getleft()
    # br = rightrotation(b)
    # a.setleft(br)
    # br = leftrotation(a)
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)


def lrrotation(node):
    r'''
        A                   A                    Cl
       / \                 / \                   / \
      B   C               B  Cl                 A   C
         / \    -->          / \    -->        / \   \
        Cl  Cr              UB  C             B  UB  Cr
        /                        \
       UB                        Cr

    UB = unbalanced node

    node = A
    '''
    # c = node.getright()
    # cl = leftrotation(c)
    # a.setright(cl)
    # cl = rightrotation(a)
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)


