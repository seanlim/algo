class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def mySubsets(depth: int):
            if depth >= len(nums):
                yield []
                return

            for deeperSubsets in mySubsets(depth + 1):
                yield deeperSubsets
                yield [nums[depth], *deeperSubsets]

        return mySubsets(0)
