"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q = deque([node])
        # root of cloned graph
        root = None
        visited = set()
        # map value to clone
        cloneMap = {}
        # map clone to values of neighbours
        cloneNeighbors = {}
        # dfs
        while q:
            n = q.popleft()
            if n in visited:
                continue
            visited.add(n)
            # create and store clone
            clone = Node(n.val, [])
            cloneMap[n.val] = clone
            cloneNeighbors[clone] = []
            # set root if needed
            if not root:
                root = clone
            if n.neighbors:
                # track values of neighbors
                cloneNeighbors[clone] = [n.val for n in n.neighbors]
                q.extend(reversed(n.neighbors))
        # populate cloned neighbor nodes
        for clone in cloneNeighbors:
           clone.neighbors = [cloneMap[n] for n in cloneNeighbors[clone]]
        return root

