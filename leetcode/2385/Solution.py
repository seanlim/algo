from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildAdj(self, rootNode):
        adj = {}
        q = deque([(rootNode, None)])
        while q:
            currNode, parentNode = q.popleft()
            adj[currNode.val] = []
            if parentNode != None:
                adj[currNode.val].append(parentNode.val)
            if currNode.left != None:
                adj[currNode.val].append(currNode.left.val)
                q.append((currNode.left, currNode))
            if currNode.right != None:
                adj[currNode.val].append(currNode.right.val)
                q.append((currNode.right, currNode))
        return adj
        
    def amountOfTime(self, root, start):
        # construct adj matrix
        adj = self.buildAdj(root)
        # bfs
        q = deque([(start, 0)])
        # track maximum timing
        maxTime = 0
        # track visited nodes
        visited = set([start])
        while q:
            curr, time = q.popleft()
            visited.add(curr)
            maxTime = max(maxTime, time)
            if (adj[curr] == []):
               continue 
            for n in adj[curr]:
                if n not in visited:
                    q.append((n, time + 1))
        return maxTime