import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def validate_binary_search_tree(root):
    return is_valid_node(root, -sys.maxint, sys.maxint)


def is_valid_node(root, lo, hi):
    if root is None:
        return True

    val = root.val
    if val < lo or hi < val:
        return False

    return is_valid_node(root.left, lo, val - 1) and is_valid_node(root.right, val + 1, hi)