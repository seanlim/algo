class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1] * N

        # prefix
        i = 0
        acc = 1
        while i < N:
            n = nums[i]
            ans[i] *= acc
            acc *= n
            i+=1

        # suffix
        i = N-1
        acc = 1
        while i >= 0:
            n = nums[i]
            ans[i] *= acc
            acc *= n
            i-=1
        return ans