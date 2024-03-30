import sys; input = sys.stdin.readline

T = int(input())
courses = [int(input()) for _ in range(int(input()))]

dp = {}

def dfs(curr, t=T):
  if t-curr == 0:
    return 1
  elif t-curr < 0:
    return 0
  t-=curr
  if t in dp:
    return dp[t]
  count = 0
  for c in courses:
    count += dfs(c, t)
  dp[t] = count
  return count

ans = 0
for c in courses:
  ans += dfs(c)

print(ans)