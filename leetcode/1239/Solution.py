class Solution(object):
    def maxLength(self, arr):
        s = set()

        def overlapping(s, str):
            return max((Counter(s) + Counter(str)).values()) > 1
        # solve with backtracking

        def backtrack(i):
            if i == len(arr):
                return len(s)
            res = 0
            if not overlapping(s, arr[i]):
                for c in arr[i]:
                    s.add(c)
                # find result if we include current string
                res = backtrack(i+1)
                for c in arr[i]:
                    s.remove(c)
            # compare best result of including this string with the next
            return max(res, backtrack(i+1))
        return backtrack(0)
