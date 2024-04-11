class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isEnd = False


    def add(self, word):
        if word[0] in self.children:
            if len(word) == 1:
                self.children[word[0]].isEnd = True
            else:
                self.children[word[0]].add(word[1:])
        else:
            t = Trie(word[0])
            if len(word) > 1:
                t.add(word[1:])
            else:
                t.isEnd = True
            self.children[word[0]] = t

    def containsWord(self, word):
        if not self.hasNext(word[0]):
            return False
        t = self.traverse(word[0])
        for c in word[1:]:
            if not t.hasNext(c):
                return False
            t = t.traverse(c)
        return t.isEnd

    def hasNext(self, c):
        return c in self.children

    def traverse(self, c):
        assert(c in self.children)
        return self.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nRows, nCols = len(board), len(board[0])
        trie = Trie()
        for w in words:
            trie.add(w)

        visited = set()
        ans = set()
        def dfs(i, j, t, word):
            if t.isEnd:
                ans.add(word)

            visited.add((i,j))
            if i-1 >= 0 and (i-1,j) not in visited and t.hasNext(board[i-1][j]):
                dfs(i-1, j, t.traverse(board[i-1][j]), word + board[i-1][j])
            if i+1 < nRows and (i+1,j) not in visited and t.hasNext(board[i+1][j]):
                dfs(i+1, j, t.traverse(board[i+1][j]), word + board[i+1][j])
            if j-1 >= 0 and (i,j-1) not in visited and t.hasNext(board[i][j-1]):
                dfs(i, j-1, t.traverse(board[i][j-1]), word + board[i][j-1])
            if j+1 < nCols and (i,j+1) not in visited and t.hasNext(board[i][j+1]):
                dfs(i, j+1, t.traverse(board[i][j+1]), word + board[i][j+1])
            visited.remove((i,j))

            return

        for i in range(nRows):
            for j in range(nCols):
                if trie.hasNext(board[i][j]):
                    dfs(i, j, trie.traverse(board[i][j]), board[i][j])

        return ans