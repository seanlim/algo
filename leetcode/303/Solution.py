class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        s = 0
        for n in nums:
            s+=n
            self.sums.append(s)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left>0 and right >0:
            return self.sums[right] - self.sums[left-1]
        else:
            return self.sums[left or right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)