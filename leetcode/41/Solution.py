class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ignore all <= 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('inf')

        # go through and flip relevant candidates
        for n in nums:
            n = abs(n)
            if n < len(nums)+1 and nums[n-1] > 0:
                nums[n-1] = -nums[n-1]

        # find first positive value, if all positive, then it is len(nums)+1
        lf = 1
        for n in nums:
            if n > 0:
                break
            lf+=1

        return lf
