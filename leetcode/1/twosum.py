class Solution(object):
    def twoSum(self, nums, target):
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        i = 0
        j = len(nums)-1
        while i < j:
            s = nums[i][1]+nums[j][1]
            if s == target:
                return [nums[i][0], nums[j][0]]
            elif s > target:
                j -= 1
            else:
                i += 1
