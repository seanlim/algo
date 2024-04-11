from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = set()

        m = len(heights)
        n = len(heights[0])

        # top right and bottom left are always part of answer
        ans.add((0, n-1))
        ans.add((m-1, 0))

        def bfs(x, y):
            q = deque([(x, y)])

            visited = set()

            pacificBreached = False
            atlanticBreached = False

            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                if (i,j) in ans:
                    return True

                # boundary detection
                if i - 1 < 0 or j - 1 < 0:
                    pacificBreached = True
                if i + 1 == m or j + 1 == n:
                    atlanticBreached = True

                if atlanticBreached and pacificBreached:
                    return True

                h = heights[i][j]

                # neighbour heights
                hL = heights[i][j-1] if j-1 >= 0 else None
                hB = heights[i+1][j] if i+1 < m else None
                hR = heights[i][j+1] if j+1 < n else None
                hT = heights[i-1][j] if i-1 >= 0 else None

                if hL != None and (i, j-1) not in visited and hL <= h:
                    q.append((i,j-1))
                if hR != None and (i, j+1) not in visited and hR <= h:
                    q.append((i,j+1))
                if hB != None and (i+1, j) not in visited and hB <= h:
                    q.append((i+1,j))
                if hT != None and (i-1, j) not in visited and hT <= h:
                    q.append((i-1,j))

            return False

        for x in range(m):
            for y in range(n):
                if (x,y) in ans:
                    continue
                if bfs(x, y):
                    ans.add((x,y))

        return ans