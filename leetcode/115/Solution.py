class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def nutsack(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if s[i] == t[j]:
                return nutsack(i+1, j+1) + nutsack(i+1, j) # take

            return nutsack(i+1, j) # don't take

        return nutsack(0, 0)
