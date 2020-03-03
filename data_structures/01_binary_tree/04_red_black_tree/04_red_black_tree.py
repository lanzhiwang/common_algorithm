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

    def remove(self, label):
        """Remove label from this tree."""
        if self.label == label:
            if self.left and self.right:
                # It's easier to balance a node with at most one child,
                # so we replace this node with the greatest one less than
                # it and remove that.
                value = self.left.get_max()
                self.label = value
                self.left.remove(value)
            else:
                # This node has at most one non-None child, so we don't
                # need to replace
                child = self.left or self.right
                if self.color == 1:
                    # This node is red, and its child is black
                    # The only way this happens to a node with one child
                    # is if both children are None leaves.
                    # We can just remove this node and call it a day.
                    if self.is_left():
                        self.parent.left = None
                    else:
                        self.parent.right = None
                else:
                    # The node is black
                    if child is None:
                        # This node and its child are black
                        if self.parent is None:
                            # The tree is now empty
                            return RedBlackTree(None)
                        else:
                            self._remove_repair()
                            if self.is_left():
                                self.parent.left = None
                            else:
                                self.parent.right = None
                            self.parent = None
                    else:
                        # This node is black and its child is red
                        # Move the child node here and make it black
                        self.label = child.label
                        self.left = child.left
                        self.right = child.right
                        if self.left:
                            self.left.parent = self
                        if self.right:
                            self.right.parent = self
        elif self.label > label:
            if self.left:
                self.left.remove(label)
        else:
            if self.right:
                self.right.remove(label)
        return self.parent or self

    def _remove_repair(self):
        """Repair the coloring of the tree that may have been messed up."""
        if color(self.sibling) == 1:
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        if (
            color(self.parent) == 0
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent._remove_repair()
            return
        if (
            color(self.parent) == 1
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent.color = 0
            return
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 0
            and color(self.sibling.left) == 1
        ):
            self.sibling.rotate_right()
            self.sibling.color = 0
            self.sibling.right.color = 1
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
            and color(self.sibling.left) == 0
        ):
            self.sibling.rotate_left()
            self.sibling.color = 0
            self.sibling.left.color = 1
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
        ):
            self.parent.rotate_left()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.left) == 1
        ):
            self.parent.rotate_right()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

    def check_color_properties(self):
        """Check the coloring of the tree, and return True iff the tree
        is colored in a way which matches these five properties:
        (wording stolen from wikipedia article)
         1. Each node is either red or black.
         2. The root node is black.
         3. All leaves are black.
         4. If a node is red, then both its children are black.
         5. Every path from any node to all of its descendent NIL nodes
            has the same number of black nodes.
        This function runs in O(n) time, because properties 4 and 5 take
        that long to check.
        """
        # I assume property 1 to hold because there is nothing that can
        # make the color be anything other than 0 or 1.

        # Property 2
        if self.color:
            # The root was red
            return False

        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.

        # Property 4
        if not self.check_coloring():
            return False

        # Property 5
        if self.black_height() is None:
            return False
        # All properties were met
        return True

    def check_coloring(self):
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        if self.color == 1:
            if color(self.left) == 1 or color(self.right) == 1:
                return False
        if self.left and not self.left.check_coloring():
            return False
        if self.right and not self.right.check_coloring():
            return False
        return True

    def black_height(self):
        r"""Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).

                   8-0
              /          \
            0-1         12-1
           /   \       /   \
        -12-0 4-0    10-0 15-0
          \         /   \
        -8-1       9-1 11-1

                                            8-0-3
                           /                                  \
                        0-1-2                                12-2
                  /              \                    /                \
             -12-0-2           4-0-2              10-0-2              15-0-2
            /       \          /   \          /            \         /     \
        NIL-0-1   -8-1-1  NIL-0-1  NIL-0-1  9-1-1         11-1-1  NIL-0-1  NIL-0-1
                  /    \                   /   \          /    \
             NIL-0-1  NIL-0-1         NIL-0-1  NIL-0-1  NIL-0-1 NIL-0-1

        """
        if self is None:
            # If we're already at a leaf, there is no path
            return 1
        left = RedBlackTree.black_height(self.left)
        right = RedBlackTree.black_height(self.right)
        if left is None or right is None:
            # There are issues with coloring below children nodes
            return None
        if left != right:
            # The two children have unequal depths
            return None
        # Return the black depth of children, plus one if this node is
        # black
        return left + (1 - self.color)

    def inorder_traverse(self):
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()

    def floor(self, label):
        """Returns the largest element in this tree which is at most label.
        This method is guaranteed to run in O(log(n)) time."""
        if self.label == label:
            return self.label
        elif self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
                else:
                    return self.label
            else:
                return self.label

    def ceil(self, label):
        """Returns the smallest element in this tree which is at least label.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self.label
        elif self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
                else:
                    return self.label
            else:
                return self.label









def color(node):
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color  # color: 0 if black, 1 if red


def test_floor_ceil():
    """Tests the floor and ceiling functions in the tree."""
    tree = RedBlackTree(0)
    for i in [-16, 16, 8, 24, 20, 22]:
        tree.insert(i)

    r"""
         0-0
      /      \
    -16-0   16-1
           /   \
          8-0 22-0
               /  \
             20-1 24-1
    """

    print(tree.floor(-20))  # None
    print(tree.floor(-10))  # -16
    print(tree.floor(8))  # 8
    print(tree.floor(50))  # 24

    print()

    print(tree.ceil(-20))  # -16
    print(tree.ceil(-10))  # 0
    print(tree.ceil(8))  # 8
    print(tree.ceil(50))  # None

    # tuples = [(-20, None, -16), (-10, -16, 0), (8, 8, 8), (50, 24, None)]
    # for val, floor, ceil in tuples:
    #     if tree.floor(val) != floor or tree.ceil(val) != ceil:
    #         return False
    return True


if __name__ == '__main__':
    print(test_floor_ceil())
