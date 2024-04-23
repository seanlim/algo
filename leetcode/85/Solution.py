class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nRows, nCols = len(matrix), len(matrix[0])
        # histogram
        hist = [0] * nCols
        ans = 0
        for row in matrix:
            for i in range(nCols):
                n = int(row[i])
                if n == 0:
                    hist[i] = 0
                else:
                    hist[i] += n
            ans = max(ans, max(hist))
            for i in range(nCols):
                n = 1  # number of columns
                j = i + 1
                while j < nCols and hist[j] != 0:
                    n += 1  # add column
                    j += 1
                    # print(n, hist[i:j])
                    ans = max(ans, min(hist[i:j]) * n)
                # print(n, hist[i:j])
                ans = max(ans, min(hist[i:j]) * n)
        return ans
