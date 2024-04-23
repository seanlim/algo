class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def edit(s):
            ans = ""
            for c in s:
                if c == "#":
                    ans = ans[:-1]
                else:
                    ans += c
            return ans

        return edit(s) == edit(t)
