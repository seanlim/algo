class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        Sliding Window

        n^2 solution involves looping over the list (for i in nums) and considering all
        subarrays where i is the left boundary. Realize that if we consider i to
        be the right boundary, we can formulate a sliding window solution with
        just 1 pass.

        """

        m = max(nums)
        ans = 0
        l = 0
        count = 0
        for r in range(len(nums)):

            # count m values until we hit enough
            if nums[r] == m:
                count+=1

            # once we have k m values, we slide l to the right until count is less than k
            while count == k:
                if nums[l] == m:
                    count-=1
                # because of 0-index, we terminate by moving l to 1 space inside the left boundary
                # of valid subarray
                l+=1

            # count is less than k at this point, and so we add the index of the
            # left boundary of the valid subarray + 1 (which is how we formulated l) to the ans
            ans+=l
        return ans
