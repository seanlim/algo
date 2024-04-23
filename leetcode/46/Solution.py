class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            n = nums[0]
            perms = perm(nums[1:])
            res = []
            for p in perms:
                for i in range(len(p) + 1):
                    res.append(p[:i] + [n] + p[i:])
            return res

        return perm(nums)
