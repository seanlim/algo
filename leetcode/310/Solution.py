from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        ans = [i for i, v in adj.items() if len(v) == 1]

        while n > 2:
            n -= len(ans)
            nAns = []
            for leaf in ans:
                u = next(iter(adj[leaf]))
                adj[u].remove(leaf)
                if len(adj[u]) == 1:
                    nAns.append(u)
            ans = nAns
        return ans
