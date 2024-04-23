class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def subset(nums):
            n = nums[0]
            if len(nums) == 1:
                return [[n], []]
            ss = subset(nums[1:])
            res = [] + ss
            for i in ss:
                if [n] + i not in res:
                    res.append([n] + i)
            return res

        return subset(nums)
