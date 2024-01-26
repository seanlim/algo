class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr, 0)
            curr += n
            ans = max(ans, curr)
        return ans
