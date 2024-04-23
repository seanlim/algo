class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j, mid = 0, len(nums) - 1, len(nums) // 2
        while j - i > 1:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                # right partition
                i = mid + 1
            else:
                # left partition
                j = mid - 1
            mid = i + (j - i) // 2
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        elif target > nums[j]:
            return j + 1
        elif target > nums[i]:
            return j
        return i
