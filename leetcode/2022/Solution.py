import math
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []
        ans = []
        for i in range(0, m*n, n):
            ans.append(original[i:i+n])
        return ans

