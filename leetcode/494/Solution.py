class Solution(object):
    def __init__(self):
        self.dp = {}

    def findTargetSumWays(self, nums, target, current=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = nums[0]
        # base case
        if len(nums[1:]) == 0:
            add = current+n
            take = current-n
            if (add, take) == (target, target):
                return 2
            if add == target:
                return 1
            if take == target:
                return 1
            return 0 
        if (len(nums[1:]), current) in self.dp:
            return self.dp[(len(nums[1:]), current)]
        numWays = 0
        numWays += self.findTargetSumWays(nums[1:], target, current + n)
        numWays += self.findTargetSumWays(nums[1:], target, current - n)
        self.dp[(len(nums[1:]), current)] = numWays
        return numWays