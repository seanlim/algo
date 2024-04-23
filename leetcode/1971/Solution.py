from collections import deque, defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            i, j = edge
            adj[i].append(j)
            adj[j].append(i)

        q = deque([source])
        visited = set()
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            if curr in visited:
                continue
            visited.add(curr)
            for i in adj[curr]:
                q.append(i)

        return False
