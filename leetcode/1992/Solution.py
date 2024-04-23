class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        h, w = len(land), len(land[0])
        islands = []

        # find islands and return the top left and bottom right
        def fillIsland(i, j):
            if i >= h or j >= w or land[i][j] != 1:
                return None
            land[i][j] = "X"
            down = fillIsland(i + 1, j)
            right = fillIsland(i, j + 1)
            if not down and not right:
                return i, j
            return down if down else right

        for i in range(h):
            for j in range(w):
                if land[i][j] == 1:
                    k, l = fillIsland(i, j)
                    islands.append([i, j, k, l])
        return islands
