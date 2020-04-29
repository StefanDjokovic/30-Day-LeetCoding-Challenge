# Very interesting and hard problem!


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def search_best(root):
    if root.right is None and root.left is None:
        return root.val, root.val

    right = None
    left = None

    if root.left is None:
        right = search_best(root.right)
        return max(right[0] + root.val, root.val), max(right[0] + root.val, root.val, right[1])

    if root.right is None:
        left = search_best(root.left)
        return max(left[0] + root.val, root.val), max(left[0] + root.val, root.val, left[1])

    right = search_best(root.right)
    left = search_best(root.left)

    b_til = max(right[0] + root.val, left[0] + root.val, root.val)
    b_best = max(right[1], left[1], right[0] + left[0] + root.val, right[0] + root.val, left[0] + root.val, root.val)

    return b_til, b_best


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return search_best(root)[1]