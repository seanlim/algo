class Solution(object):
    def rob(self, nums):
        # we store the sum of the n-1th and n-2th values
        previous_sum = 0
        preceding_sum = 0

        for n in nums:
            # we can either:
            # 1. rob the current house and pick previous sum
            # 2. don't rob the current house and pic the preceding sum
            choice = max(n + previous_sum,  preceding_sum)
            previous_sum = preceding_sum
            preceding_sum = choice

        # when the for-loop terminates, we will always have
        # preceding sum as the best choice
        return preceding_sum
