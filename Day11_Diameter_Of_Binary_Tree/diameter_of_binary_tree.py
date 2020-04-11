# Fun little one, apparently it "beats 86.70% of python3 submissions"
# The idea is to return two values: the first indicates the length of the longest path from that node to a leaf
# the second is the best distance value found below that node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def max_dist(root):
    max_of_all = 0
    own_max = 0

    if root.left is not None:
        val_left = max_dist(root.left)
        if own_max < val_left[0] + 1:
            own_max = val_left[0] + 1
        if max_of_all < val_left[1]:
            max_of_all = val_left[1]
    if root.right is not None:
        val_right = max_dist(root.right)
        if max_of_all < val_right[1]:
            max_of_all = val_right[1]
        if max_of_all < own_max + val_right[0] + 1:
            max_of_all = own_max + val_right[0] + 1
        if own_max < val_right[0] + 1:
            own_max = val_right[0] + 1

    return [own_max, max_of_all]


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None or root.left is None and root.right is None:
            return 0

        val = max_dist(root)
        return max(val)