# A disappointing last problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def search(root, arr):
    if len(arr) == 1 and root.val == arr[0]:
        if root.right is None and root.left is None:
            return True
        else:
            return False
    if root.left is not None and root.left.val == arr[1]:
        if search(root.left, arr[1:]):
            return True
    if root.right is not None and root.right.val == arr[1]:
        if search(root.right, arr[1:]):
            return True

    return False


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return search(root, arr)