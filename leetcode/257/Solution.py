# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node, path):
            if node.left:
                dfs(node.left, path + f"->{node.left.val}")
            if node.right:
                dfs(node.right, path + f"->{node.right.val}")
            if not node.left and not node.right:
                paths.append(path)
        if root: dfs(root, f"{root.val}")
        return paths

