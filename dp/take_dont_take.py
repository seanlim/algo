l = [5, 9, -4, 1, 2]
# 17

# given a list of numbers, find the maximum consequetive sequence you can pick,
# skipping at most 1 element
dp = {}
def findMaxSequence(l, skipped=False):
    n = len(l)
    max_sub = 0
    if str(l) in dp:
        return dp[str(l)]
    for i in range(n):
        take = l[i] + findMaxSequence(l[i+1:], skipped=False)
        dont_take = l[i] + findMaxSequence(l[i+2:], skipped=True)
        max_sub = max(take if skipped else max(take, dont_take), max_sub)
    dp[str(l)] = max_sub
    return max_sub

print(findMaxSequence(l))
