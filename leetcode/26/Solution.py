class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                continue
            i+=1
        return nums



