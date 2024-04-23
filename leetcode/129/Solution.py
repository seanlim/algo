import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node, depth=0, sum=0):
            if not node:
                return 0
            sum += node.val * math.pow(10, -depth)
            if not node.left and not node.right:
                return sum * math.pow(10, depth)
            leftSum = traverse(node.left, depth + 1, sum)
            rightSum = traverse(node.right, depth + 1, sum)
            return leftSum + rightSum

        return round(traverse(root))
