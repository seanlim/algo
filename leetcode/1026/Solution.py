# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildAncestors(self, node, ancestors):
        # print("node %i" % node.val)
        # print(ancestors)
        maxDiff = 0
        maxDiffLeft = 0
        maxDiffRight = 0 
        for a in ancestors:
            maxDiff = max(maxDiff, abs(node.val - a))
        # go to children
        if node.right != None:
            maxDiffRight = self.buildAncestors(node.right, ancestors + [node.val])
        if node.left != None:
            maxDiffLeft = self.buildAncestors(node.left, ancestors + [node.val])
        return max([maxDiff, maxDiffLeft, maxDiffRight])

    def maxAncestorDiff(self, root):
        return self.buildAncestors(root, [])
