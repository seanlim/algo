# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumNodes(node, isLeft=False):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            left = sumNodes(node.left, True)
            right = sumNodes(node.right, False)
            return left + right

        return sumNodes(root)
