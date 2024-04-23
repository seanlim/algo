class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        ans = nums[0]
        for n in nums:
            if n == ans:
                i += 1
            else:
                i -= 1
            if i == 0:
                ans = n
                i = 1
        return ans
