# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxD = 0
        def findHeight(node):
            if node is None:
                return 0
            left = findHeight(node.left)
            right = findHeight(node.right)
            self.maxD = max(self.maxD, left+right)
            return 1+max(left, right)
        findHeight(root)
        return self.maxD
