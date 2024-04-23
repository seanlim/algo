class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])

        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    continue
                if i - 1 >= 0:  # up
                    if grid[i - 1][j] == 0:
                        ans += 1
                else:
                    ans += 1
                if i + 1 < height:  # down
                    if grid[i + 1][j] == 0:
                        ans += 1
                else:
                    ans += 1
                if j - 1 >= 0:  # left
                    if grid[i][j - 1] == 0:
                        ans += 1
                else:
                    ans += 1
                if j + 1 < width:  # right
                    if grid[i][j + 1] == 0:
                        ans += 1
                else:
                    ans += 1
        return ans
