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
    需要左旋转的情况：左子树的高度 - 右子树的高度 = 2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    2             0
    3             1
    4             2
    ...

            A              B
           /              / \
          B       -->    UB  A
         /
        UB


        7-2 node         6-2            6-2
        /               /  \            /  \
      6-2 ret          5-1 7-2         5-1 7-1
      /
     5-1

    #######################################################

            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB


            A-3                         B-3                      B-3
           /   \                       /    \                   /    \
          B-3   C-1                  Bl-2   A-3                Bl-2   A-2
         /   \            -->        /      / \                /      / \
        Bl-2 Br-1                 UB-1   Br-1  C-1           UB-1   Br-1  C-1
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
    需要右旋转的情况：左子树的高度 - 右子树的高度 = -2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    0            2
    1            3
    2            4
    ...

     A                      C
      \                    / \
       C       -->        A   Cr
        \
         Cr

    7-2 node           8-2             8-2
      \               /   \            / \
      8-2 ret        7-2  9-1        7-1  9-1
        \
        9-1

    #######################################################

        A                      C
       / \                    / \
      B   C                  A   Cr
         / \       -->      / \   \
        Cl  Cr             B  Cl  UB
             \
             UB


         A-3                         C-3                   C-3
       /    \                       /    \                /   \
      B-1   C-3                    A-3   Cr-2           A-2    Cr-2
            / \       -->         /  \     \           /  \     \
         Cl-1  Cr-2             B-1  Cl-1  UB-1      B-1  Cl-1  UB-1
                \
                UB-1


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
    需要先右旋转，再左旋转的情况：左子树的高度 - 右子树的高度 = 2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    2             0
    3             1
    4             2
    ...

      A                 A          UB
     /                 /          /  \
    B       -->       UB   -->   B    A
     \               /
      UB            B


      5-2               5-2         4-2
     /                 /            /  \
    3-2       -->     4-2   -->    3-1 5-1
     \               /
      4-1           3-1

    #######################################################

            A              A                    Br
           / \            / \                  /  \
          B   C    RR    Br  C       LR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C
             \        /
             UB     Bl

    RR = rightrotation   LR = leftrotation

              A-3               A-3                       Br-3
             /   \             /   \                   /       \
           B-3   C-1    RR    Br-3  C-1     LR       B-2       A-2
         /    \       -->     /  \         -->        /       /   \
        Bl-1  Br-2          B-2   UB-1              Bl-1    UB-1  C-1
                \            /
                UB-1       Bl-1

    '''
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)


def lrrotation(node):
    r"""
    需要先左旋转，再右旋转的情况：左子树的高度 - 右子树的高度 = -2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    0             2
    1             3
    2             4
    ...

     A            A                  B
      \            \                / \
       C     -->    B     -->      A   C
      /              \
     B                C

     A-2            A-2                   B-2
      \               \                  /   \
       C-2     -->    B-2     -->      A-1   C-1
      /                 \
     B-1                C-1

    #######################################################

        A                   A                    Cl
       / \                 / \                   / \
      B   C               B  Cl                 A   C
         / \    -->          / \    -->        / \   \
        Cl  Cr              UB  C             B  UB  Cr
        /                        \
       UB                        Cr

    UB = unbalanced node

             A-3                        A-3                        Cl-3
            /  \                      /    \                      /     \
         B-1   C-3                   B-1  Cl-3                  A-2     C-2
             /    \    -->                /   \         -->    /   \      \
           Cl-2  Cr-1                   UB-1  C-2             B-1  UB-1  Cr-1
           /                                    \
         UB-1                                  Cr-1

    """
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)
