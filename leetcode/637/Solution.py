""" NOTES:
Question input format makes it difficult to iteratively loop through
levels of the tree with 2 ** height because "null" entries for a
node's children are selectively ommitted when both children are "null".

For instance, using brackets to demarcate level, question input
states "[(3),(null,30),(10,null)]" when it should be
"[(3), (null, 30), (null, null, 10, null)]".
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = {}
        def walk(node, l):
            if not node:
                return
            if l in levels :
                levels[l].append(node.val)
            else:
                levels[l] = [node.val]
            walk(node.left, l+1)
            walk(node.right, l+1)
        walk(root, 0)
        ans = []
        for l in levels:
            vals = levels[l]
            ans.append(float(sum(vals))/len(vals))
        return ans
