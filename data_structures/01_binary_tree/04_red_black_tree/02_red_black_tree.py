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

    def insert(self, label):
        if self.label is None:
            # Only possible with an empty tree
            self.label = label
            return self

        if label == self.label:
            return self

        elif label < self.label:
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                self.left._insert_repair()

        else:  # label > self.label
            if self.right:
                self.right.insert(label)
            else:
                self.right = RedBlackTree(label, 1, self)
                self.right._insert_repair()

        return self.parent or self

    def _insert_repair(self):
        """Repair the coloring from inserting into a tree."""
        if self.parent is None:
            # This node is the root, so it just needs to be black
            self.color = 0
        elif color(self.parent) == 0: # 有父节点，父节点是黑色
            # If the parent is black, then it just needs to be red
            # 新节点的父节点是黑色，在这种情形下，树仍是有效的，只需要保证新节点为红色即可
            self.color = 1
        else:  # 有父节点，父节点是红色
            uncle = self.parent.sibling  # 父节点的兄弟节点，也就是新节点的叔父节点
            if color(uncle) == 0:  # 叔父节点为黑色或者没有叔父节点
                # 将要插入的节点标为N，N的父节点标为P，N的祖父节点标为G，N的叔父节点标为U
                r"""
                情景一：            情景二：
                G        G        |    G          G
                 \        \       |   /          /
                  p  ->    N      |  P    ->    N
                 /          \     |   \        /
                N            p    |    N      P

                情景三：            情景四：
                    G        P    |  G            P
                   /        / \   |   \          / \
                  P    ->  N   G  |    P    ->  G   N
                 /                |     \
                N                 |      N

                """
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    self.left._insert_repair()
                elif self.is_left():
                    self.grandparent.rotate_right()
                    self.parent.color = 0
                    self.parent.right.color = 1
                else:
                    self.grandparent.rotate_left()
                    self.parent.color = 0
                    self.parent.left.color = 1

            else:  # 叔父节点为红色
                self.parent.color = 0  # 父节点变为黑色
                uncle.color = 0  # 叔父节点变为黑色
                self.grandparent.color = 1  # 祖父节点变为红色
                self.grandparent._insert_repair()  # 祖父节点进行重新修正

    @property
    def grandparent(self):
        """Get the current node's grandparent, or None if it doesn't exist."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    @property
    def sibling(self):
        """Get the current node's sibling, or None if it doesn't exist."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self):
        """Returns true iff this node is the left child of its parent."""
        return self.parent and self.parent.left is self

    def is_right(self):
        """Returns true iff this node is the right child of its parent."""
        return self.parent and self.parent.right is self

    def __contains__(self, label):
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        Guaranteed to run in O(log(n)) time.
        """
        return self.search(label) is not None

    def search(self, label):
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self
        elif label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        else:
            if self.left is None:
                return None
            else:
                return self.left.search(label)


def color(node):
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color  # 0 黑色, 1 红色


r"""
####################################################
insert(self=root, label)
    insert(self=root.left, label)
    insert(self=root.right, label)
    O -> self
     \
      O
       \
        O
         \
          O
           \
            O -> RedBlackTree(label, 1, self)
    return self.parent or self


####################################################
insert(self=root.left, label)
    insert(self=root.left.left, label)
    insert(self=root.left.right, label)

insert(self=root.right, label)
    insert(self=root.right.left, label)
    insert(self=root.right.right, label)
    O
     \
      O -> self
       \
        O
         \
          O
           \
            O -> RedBlackTree(label, 1, self)
    return self.parent or self


####################################################
insert(self=root.left.left, label)
    insert(self=root.left.left.left, label)
    insert(self=root.left.left.right, label)

insert(self=root.left.right, label)
    insert(self=root.left.right.left, label)
    insert(self=root.left.right.right, label)

insert(self=root.right.left, label)
    insert(self=root.right.left.left, label)
    insert(self=root.right.left.right, label)

insert(self=root.right.right, label)
    insert(self=root.right.right.left, label)
    insert(self=root.right.right.right, label)
    O
     \
      O
       \
        O -> self
         \
          O
           \
            O -> RedBlackTree(label, 1, self)
    return self.parent or self


####################################################
insert(self=root.left.left.left, label)
insert(self=root.left.left.right, label)
insert(self=root.left.right.left, label)
insert(self=root.left.right.right, label)
insert(self=root.right.left.left, label)
insert(self=root.right.left.right, label)
insert(self=root.right.right.left, label)
insert(self=root.right.right.right, label)
    self.right = RedBlackTree(label, 1, self)  # 新节点为红色
    self.right._insert_repair()
    O
     \
      O
       \
        O
         \
          O -> self
           \
            O -> RedBlackTree(label, 1, self)
    return self.parent or self

"""


def test_insert():
    tree = RedBlackTree(0)
    for i in [8, -8, 4, 12, 10, 11]:
        tree = tree.insert(i)

    r"""

         0-0
      /      \
    -8-0    8-1
           /   \
         4-0   11-0
               /   \
             10-1  12-1

    """
    ans = RedBlackTree(0, 0)
    ans.left = RedBlackTree(-8, 0, ans)
    ans.right = RedBlackTree(8, 1, ans)
    ans.right.left = RedBlackTree(4, 0, ans.right)
    ans.right.right = RedBlackTree(11, 0, ans.right)
    ans.right.right.left = RedBlackTree(10, 1, ans.right.right)
    ans.right.right.right = RedBlackTree(12, 1, ans.right.right)
    return tree == ans


def test_insert_and_search():
    """Tests searching through the tree for values."""
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    if 5 in tree or -6 in tree or -10 in tree or 13 in tree:
        # Found something not in there
        return False
    if not (11 in tree and 12 in tree and -8 in tree and 0 in tree):
        # Didn't find something in there
        return False
    return True


if __name__ == '__main__':
    print(test_insert())
    print(test_insert_and_search())
