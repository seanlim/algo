# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        def isSame(r, sr):
            if not r or not sr:
                return (not r and not sr)
            if r.val != sr.val:
                return False
            leftSame = isSame(r.left, sr.left)
            rightSame = isSame(r.right, sr.right)
            return leftSame and rightSame
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
