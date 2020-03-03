#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RedBlackTree:
    def __init__(self, label=None, color=0, parent=None, left=None, right=None):
        self.label = label
        self.color = color  # 0 黑色, 1 红色, 默认黑色
        self.parent = parent
        self.left = left
        self.right = right

    def rotate_left(self):
        r"""
        情景一：
                0 -> self parent = None
            /      \
          -10      10 -> right
          / \     /  \
        -20 -5   5   20

                10
               /  \
              0   20
            /  \
          -10   5
          / \
        -20 -5

        情景二：
                0 -> parent
            /      \
          -10      10 -> self
          / \     /  \
        -20 -5   5   20 -> right

               0
            /     \
          -10     20
          / \    /
        -20 -5  10
                /
               5

        """
        parent = self.parent
        right = self.right
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right

    def rotate_right(self):
        r"""
        情景一：
                  10 -> self parent = None
                 /  \
        left <- 0    20
              /   \
            -10    5
            / \
          -20 -5

                0
             /     \
           -10     10
          /  \    /  \
        -20  -5  5   20

        情景二：
                   0 -> parent
             /          \
           -10          10 -> self
          /  \    /          \
        -20  -5  5 -> left   20

                0
             /     \
           -10      5
          /  \       \
        -20  -5       10
                       \
                       20

        """
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left:
            self.left.parent = self
        self.parent = left
        left.right = self
        if parent is not None:
            if parent.right is self:
                parent.right = left
            else:
                parent.left = left
        left.parent = parent
        return left

    def __eq__(self, other):
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            return False


def test_rotations():
    r"""Test that the rotate_left and rotate_right functions work.

            0
        /      \
      -10      10
      / \     / \
    -20 -5   5  20

            10
           /  \
          0   20
        /  \
      -10  5
      / \
    -20 -5

    """
    # Make a tree to test on
    tree = RedBlackTree(0)
    tree.left = RedBlackTree(-10, parent=tree)
    tree.right = RedBlackTree(10, parent=tree)
    tree.left.left = RedBlackTree(-20, parent=tree.left)
    tree.left.right = RedBlackTree(-5, parent=tree.left)
    tree.right.left = RedBlackTree(5, parent=tree.right)
    tree.right.right = RedBlackTree(20, parent=tree.right)

    # Make the right rotation
    left_rot = RedBlackTree(10)
    left_rot.left = RedBlackTree(0, parent=left_rot)
    left_rot.right = RedBlackTree(20, parent=left_rot)
    left_rot.left.left = RedBlackTree(-10, parent=left_rot.left)
    left_rot.left.right = RedBlackTree(5, parent=left_rot.left)
    left_rot.left.left.left = RedBlackTree(-20, parent=left_rot.left.left)
    left_rot.left.left.right = RedBlackTree(-5, parent=left_rot.left.left)
    tree = tree.rotate_left()
    if tree != left_rot:
        return False

    tree = tree.rotate_right()
    tree = tree.rotate_right()
    # Make the left rotation
    r"""

            10
           /  \
          0   20
        /  \
      -10  5
      / \
    -20 -5

           0
        /     \
      -10     10
      / \    / \
    -20 -5  5  20

       -10
     /    \
    -20    0
          / \
         -5 10
            / \
            5 20

    """
    right_rot = RedBlackTree(-10)
    right_rot.left = RedBlackTree(-20, parent=right_rot)
    right_rot.right = RedBlackTree(0, parent=right_rot)
    right_rot.right.left = RedBlackTree(-5, parent=right_rot.right)
    right_rot.right.right = RedBlackTree(10, parent=right_rot.right)
    right_rot.right.right.left = RedBlackTree(5, parent=right_rot.right.right)
    right_rot.right.right.right = RedBlackTree(20, parent=right_rot.right.right)
    if tree != right_rot:
        return False
    return True


if __name__ == '__main__':
    print(test_rotations())
