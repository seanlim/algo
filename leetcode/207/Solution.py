class Solution(object):
    def canFinish(self, n, p):
        """
        :type n: int
        :type p: List[List[int]]
        :rtype: bool
        """
        g = [[] for _ in range(n)]
        for edge in p:
            ai, bi = edge
            if ai == bi:
                return False
            g[bi].append(ai)
        visit = set()
        def dfs(curr):
            if curr in visit:
                return False
            if not g[curr]:
                return True
            visit.add(curr)
            for d in g[curr]:
                if not dfs(d):
                    return False
            visit.remove(curr)
            g[curr] = []
            return True
        for c, deps in enumerate(g):
            if deps and not dfs(c):
                return False
        return True




