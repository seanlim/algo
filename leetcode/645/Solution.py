class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        list_sum = sum(nums)
        set_sum = sum(set(nums))
        # calculate the expected sum of all numbers from 1 to n
        expected_sum = n * (n + 1) // 2
        # idea: use difference in sums of set and list to solve
        # to find the repeated number, we take the difference between list and set
        # to find the missing number, we take the difference between expected sum and set sum
        return list_sum-set_sum, expected_sum-set_sum
