class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        nums.sort()
        p = nums[0]
        i = 1
        while i < n:
            if nums[i] == p:
                return True
            p = nums[i]
            i += 1
