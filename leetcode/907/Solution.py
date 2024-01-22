class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9+7
        # dp[i] = sum of subarrays ending at i
        dp = [0]*n
        # monotonic stack of the indices of current working values
        stack = []
        res = 0
        for i in range(n):
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                stack.pop()
            # the current number is less than all elements between i and
            # the element at the top of the stack
            if len(stack) > 0:
                # if there is an element at the top of the stack, we calc the
                # solution at i by using the solution to the element at the top of stack
                last_index = stack[-1]
                dp[i] = dp[last_index]+arr[i]*(i-last_index)
            else:
                # if the stack is empty,there are no elements up to i that are
                # smaller than the number at i, all (i + 1) contiguous combinations will have arr[i] as minimum
                dp[i] = arr[i]*(i+1)
            stack.append(i)
            res = (res+dp[i]) % mod
        return res
