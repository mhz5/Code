class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def to_bin_search_tree(nums):
    if not nums:
        return None

    mid = len(nums) / 2
    root = TreeNode(nums[mid])
    root.left = to_bin_search_tree(nums[:mid])
    root.right = to_bin_search_tree(nums[mid + 1:])

    return root
