# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None or root2 is None:
            return root1 if root2 is None else root2

        # merge into node1
        def merge(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            node1.val += node2.val
            node1.left = merge(node1.left, node2.left)
            node1.right = merge(node1.right, node2.right)
            return node1


        merge(root1, root2)

        return root1
