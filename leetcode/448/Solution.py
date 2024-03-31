class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] *= -1
        return [i+1 for i,n in enumerate(nums) if n > 0]
