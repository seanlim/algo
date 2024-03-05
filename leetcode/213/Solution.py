class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return max(nums)
        def robbers(nums):
            prev = 0
            prevprev = 0
            res = 0
            for n in nums:
                rob = n + prevprev
                dont_rob = prev
                res = max(rob, dont_rob)
                prev, prevprev =  res, prev
            return res
        ans = max(
            robbers(nums[1:]),
            robbers(nums[:-1]),
        )
        return ans

