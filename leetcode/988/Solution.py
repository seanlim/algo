# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        i_dict = {i: chr(i + 97) for i in range(26)}

        def cmp(l, r):
            i, j = len(l) - 1, len(r) - 1
            while i > -1 and j > -1:
                if l[i] < r[j]:
                    return l
                if r[j] < l[i]:
                    return r
                i -= 1
                j -= 1
            return l if len(l) < len(r) else r

        def bfs(node, path=[]):
            left, right = [], []
            if node.left:
                left = bfs(node.left, path + [node.val])
            if node.right:
                right = bfs(node.right, path + [node.val])
            if not node.left and not node.right:
                return path + [node.val]
            if left and right:
                # print([i_dict[i] for i in left], [i_dict[i] for i in right])
                # print(left,right)
                return cmp(left, right)
            return right if right else left

        ans = ""
        for i in reversed(bfs(root)):
            ans += i_dict[i]
        return ans
