# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# a non-optimized version (doesn't use the "preorder" information, but just put everything in the tree iteratively)
def insertion(root, x):
    if root.val > x:
        if root.left == None:
            root.left = TreeNode(x)
        else:
            insertion(root.left, x)
    else:
        if root.right == None:
            root.right = TreeNode(x)
        else:
            insertion(root.right, x)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        del preorder[0]
        while len(preorder) > 0:
            insertion(root, preorder[0])
            del preorder[0]

        return root
