class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        @cache
        def perm(nums, curr):
            if len(nums) == 0:
                ans.append(curr)
                return
            for i in range(len(nums)):
                perm(nums[:i] + nums[i + 1 :], curr + (nums[i],))

        perm(tuple(nums), ())
        return ans
