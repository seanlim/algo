class Solution(object):
    def threeSum(self, nums):
        res = set()
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            k = len(nums) - 1
            if i > len(nums) - 2:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    break
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                    continue
                elif s > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res
