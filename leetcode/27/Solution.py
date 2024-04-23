class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = len([n for n in nums if n != val])
        while i < j:
            if nums[i] == val:
                # find from back
                while nums[j] == val and i < j:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return k
