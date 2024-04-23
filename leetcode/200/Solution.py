class Solution(object):
    def numIslands(self, grid):
        h = len(grid)
        w = len(grid[0])

        def explore(i, j):
            grid[i][j] = "X"
            if j + 1 < w and grid[i][j + 1] == "1":
                # move right
                explore(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                # move left
                explore(i, j - 1)
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                # move up
                explore(i - 1, j)
            if i + 1 < h and grid[i + 1][j] == "1":
                # move down
                explore(i + 1, j)
            return

        counter = 0
        for i in range(0, h):
            for j in range(0, w):
                cell = grid[i][j]
                if cell == "0":
                    continue
                if cell == "1":
                    counter += 1
                    # new land
                    explore(i, j)
        return counter
