class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0, 1, 1, 2]
        if n <= 3:
            return dp[:n+1]
        while len(dp) < n+1:
            chunk = []
            for i in dp:
                chunk.append(i+1)
                if len(chunk) + len(dp) == n+1:
                    return dp+chunk
            dp+=chunk
        return dp[:n+1]

            