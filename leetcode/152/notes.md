# [Maximum product subarray](https://leetcode.com/problems/maximum-product-subarray/description/)

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        ans: the maximum value for [0-n] subarray
        cMax: the maximum value we can obtain at the nth step
        cMin: the minimum value we can obtain at the nth step
        """
        ans,cMax,cMin=max(nums),1,1
        for n in nums:
            if n == 0:
                # reset cMax and cMin to 1 since 0 breaks our "streak"
                cMax, cMin = 1, 1
                continue
            choice = (cMax*n, cMin*n, n)
            cMax=max(choice)
            cMin=min(choice)

            ans = max(ans, cMax)
        return ans
```
