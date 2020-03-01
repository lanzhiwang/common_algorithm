class Node:
    """This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display(tree):
    """In Order traversal of the tree
    """
    if tree is None:
        return

    if tree.left is not None:
        display(tree.left)

    print(tree.data)

    if tree.right is not None:
        display(tree.right)

    return


def depth_of_tree(tree):
    """This is the recursive function to find the depth of binary tree.
    """
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree):
    """This functions returns that is it full binary tree or not?
    """
    if tree is None:
        return True

    if (tree.left is None) and (tree.right is None):
        return True

    if (tree.left is not None) and (tree.right is not None):
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return False


def main():
    r"""Main func for testing.

         1
      /    \
     2      3
    / \    /
   4   5  7
      /  /
     6  8
         \
          9

    """
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)

    tree.left.left = Node(4)
    tree.left.right = Node(5)

    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is: ")
    display(tree)


if __name__ == '__main__':
    main()

r"""

         1
      /    \
     2      3
    / \    /
   4   5  6
      /  /
     7  8
         \
          9

depth_of_tree(1)
    depth_of_tree(2)  # return 3
    depth_of_tree(3)  # return 4
    return 1 + max(3, 4) = 5

depth_of_tree(2)
    depth_of_tree(4)  # return 1
    depth_of_tree(5)  # return 2
    return 1 + max(1, 2) = 3

depth_of_tree(3)
    depth_of_tree(6)  # return 3
    depth_of_tree()  # return 0
    return 1 + max(3, 0) = 4

depth_of_tree(4)
    depth_of_tree()  # return 0
    depth_of_tree()  # return 0
    return 1 + max(0, 0) = 1

depth_of_tree(5)
    depth_of_tree(7)  # return 1
    depth_of_tree()  # return 0
    return 1 + max(1, 0) = 2

depth_of_tree(6)
    depth_of_tree(8)  # return 2
    depth_of_tree()  # return 0
    return 1 + max(2, 0) = 3

depth_of_tree(7)
    depth_of_tree()  return 0
    depth_of_tree()  return 0
    return 1 + max(0, 0) = 1

depth_of_tree(8)
    depth_of_tree()  return 0
    depth_of_tree(9) return 1
    return 1 + max(0, 1) = 2

depth_of_tree(9)
    depth_of_tree()  return 0
    depth_of_tree()  return 0
    return 1 + max(0, 0) = 1

depth_of_tree()
    return 0
"""

r"""

         1
      /    \
     2      3
    / \    / \
   4   5  6   7
  / \    /
 8   9  10


is_full_binary_tree(1)
    is_full_binary_tree(2)  # return True
    is_full_binary_tree(3)  # return False
    return False

is_full_binary_tree(2)
    is_full_binary_tree(4)  # return True
    is_full_binary_tree(5)  # return True
    return True

is_full_binary_tree(3)
    is_full_binary_tree(6)  # return False
    is_full_binary_tree(7)  # return True
    return False

is_full_binary_tree(4)
    is_full_binary_tree(8)  # return True
    is_full_binary_tree(9)  # return True
    return True

is_full_binary_tree(5)
    return True

is_full_binary_tree(6)
    return False

is_full_binary_tree(7)
    return True

is_full_binary_tree(8)
    return True

is_full_binary_tree(9)
    return True

"""