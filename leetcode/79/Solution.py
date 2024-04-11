class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nRows, nCols = len(board), len(board[0])

        visited = set()

        def dfs(i,j, path):
            if path not in word:
                return False
            if len(path) >= len(word):
                return path == word

            visited.add((i,j))
            if i-1 >= 0 and (i-1,j) not in visited:
                if dfs(i-1, j, path+board[i-1][j]):
                    return True
            if i+1 < nRows and (i+1,j) not in visited:
                if dfs(i+1,j, path+board[i+1][j]):
                    return True
            if j-1 >=0 and (i, j-1) not in visited:
                if dfs(i, j-1, path+board[i][j-1]):
                    return True
            if j+1 < nCols and (i, j+1) not in visited:
                if dfs(i, j+1, path+board[i][j+1]):
                    return True
            visited.remove((i,j))

            return False

        for i in range(nRows):
            for j in range(nCols):
                if board[i][j] == word[0] and dfs(i, j, board[i][j]):
                    return True

        return False