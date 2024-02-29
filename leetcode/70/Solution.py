class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        n0=1
        n1=2
        for _ in range(n - 2):
            n2 = n0 + n1
            n0, n1 = n1, n2
        return n1