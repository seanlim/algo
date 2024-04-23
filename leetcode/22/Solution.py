class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        ans = []

        def gen(cnt, s):
            if cnt < 0 or cnt > n or len(s) > n * 2:
                return
            if len(s) == n * 2 and cnt == 0:
                ans.append(s)
            if cnt > 0:
                gen(cnt - 1, s + ")")
            gen(cnt + 1, s + "(")

        gen(1, "(")
        return ans
