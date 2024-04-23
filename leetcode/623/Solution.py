# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        def traverse(node, d=1, isLeft=False):
            if d == depth:
                newNode = TreeNode(val)
                if isLeft:
                    newNode.left = node
                else:
                    newNode.right = node
                return newNode

            if not node:
                return None

            goLeft = traverse(node.left, d + 1, True)
            goRight = traverse(node.right, d + 1, False)

            if goLeft != None:
                node.left = goLeft
            if goRight != None:
                node.right = goRight

        newRoot = traverse(root, 1, True)
        if newRoot != None:
            return newRoot
        return root
